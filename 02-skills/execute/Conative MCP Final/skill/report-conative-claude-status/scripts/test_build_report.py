"""Regression checks for current testcase-based bug attribution."""
import copy
import unittest

from build_report import prepare, render


def source(name='Shopify', status='PASSED'):
    return {'name': name, 'product': [status], 'variant': ['']}


def case(org, actual='FAIL', tickets=None, matches=None):
    result = {'org': org, 'source': 'Shopify', 'tc_id': 'T2-COV-001',
              'actual': actual, 'ticket_ids': tickets or [],
              'failure_evidence': 'Forecast starts one day after org-local today; expected end unchanged.'}
    if matches is not None:
        result['matched_tickets'] = matches
    return result


def match(ticket='12345'):
    return {'ticket_id': ticket,
            'ticket_reference': f'https://devtak.cbidigital.com/work_packages/{ticket}/activity',
            'reason': 'Verified ticket Actual/Expected and testcase show the same one-day-late forecast start.'}


def fixture():
    return {'organizations': [{'name': n, 'sources': [source()]}
                              for n in ['Org A', 'Org B', 'Org C', 'Org D']],
            'bugs': [{'id': '12345', 'title': 'Verified defect', 'orgs': ['Org A']},
                     {'id': '99999', 'title': 'Old ticket', 'orgs': ['Org C']}],
            'testcases': [case('Org A', tickets=['12345']),
                          case('Org B', matches=[match()]),
                          case('Org C', actual='PASS', tickets=['12345', '99999']),
                          case('Org D')],
            'limitations': [], 'bug_scan_complete': True}


class BugEvidenceTests(unittest.TestCase):
    def test_add_org_from_verified_case_without_ticket_or_field_failure(self):
        orgs, bugs, gaps = prepare(fixture())
        self.assertEqual(bugs['12345']['orgs'], {'Org A', 'Org B'})
        self.assertEqual(bugs['12345']['evidence'][1]['link_type'], 'defect-match')
        self.assertTrue(all(o['status'] == 'PASS' for o in orgs))
        self.assertTrue(any('Field compare' in g for g in gaps))

    def test_pass_stale_ticket_and_unmatched_shared_symptom_do_not_add_org(self):
        _, bugs, gaps = prepare(fixture())
        self.assertNotIn('Org C', bugs['12345']['orgs'])
        self.assertNotIn('Org D', bugs['12345']['orgs'])
        self.assertNotIn('99999', bugs)
        self.assertTrue(any('Org D' in g for g in gaps))

    def test_report_counts_colors_and_deduplication(self):
        report = render(fixture())
        self.assertEqual(report.count('12345 - Verified defect'), 1)
        self.assertIn('ORG: Org A / Org B', report)
        self.assertIn('Source: Shopify - 🟢 PASS', report)
        self.assertEqual(report.count('Product: TOTAL: 1 fields'), 4)
        self.assertEqual(report.count('Variant: TOTAL: 0 fields'), 4)

    def test_missing_testcase_scan_rejected(self):
        data = fixture(); del data['testcases']
        with self.assertRaises(ValueError): prepare(data)

    def test_duplicate_and_out_of_scope_cases_rejected(self):
        for mutate in [lambda d: d['testcases'].append(copy.deepcopy(d['testcases'][0])),
                       lambda d: d['testcases'][0].update(source='Wrong source')]:
            data = fixture(); mutate(data)
            with self.assertRaises(ValueError): prepare(data)

    def test_missing_failure_proof_or_match_reason_rejected(self):
        for key in ['failure_evidence', 'reason']:
            data = fixture()
            if key == 'reason': del data['testcases'][1]['matched_tickets'][0][key]
            else: del data['testcases'][0][key]
            with self.assertRaises(ValueError): prepare(data)

    def test_match_must_identify_exact_ticket(self):
        data = fixture()
        data['testcases'][1]['matched_tickets'][0]['ticket_reference'] = 'https://devtak.cbidigital.com/work_packages/54321'
        with self.assertRaises(ValueError): prepare(data)

    def test_different_explicit_ticket_not_silently_reassigned(self):
        data = fixture(); data['testcases'][1]['ticket_ids'] = ['54321']
        with self.assertRaises(ValueError): prepare(data)

    def test_ambiguous_explicit_link_is_excluded_with_limitation(self):
        data = fixture(); data['bug_scan_complete'] = False
        data['testcases'][0].update(excluded_ticket_ids=['12345'], limitation='Org A ticket link describes a different failure; review needed.')
        _, bugs, gaps = prepare(data)
        self.assertEqual(bugs['12345']['orgs'], {'Org B'})
        self.assertTrue(any('review needed' in g for g in gaps))

    def test_ambiguous_link_cannot_claim_complete_scan(self):
        data = fixture()
        data['testcases'][0].update(excluded_ticket_ids=['12345'], limitation='Review needed')
        with self.assertRaises(ValueError): prepare(data)


if __name__ == '__main__':
    unittest.main()
