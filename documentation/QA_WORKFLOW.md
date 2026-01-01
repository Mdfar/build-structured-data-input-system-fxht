Mineral Metrics QA Workflow SOP
1. Analyst Level (Blind Entry)

Analyst A and Analyst B log into separate Retool portals.

They see the same Source PDF but cannot see any data in the 'Submission' table.

Both must submit all fields (Tonnes, Grade, Category).

2. Comparison Layer

The system checks Submission_Hash.

If hashes match: Status -> Human Matched.

If hashes differ: Status -> Conflict Flagged (Alerts Senior Admin).

3. AI Triple-Lock

Human Matched records are sent to vision_check.py.

GPT-4o scans the PDF image to confirm the text matches the entered numbers.

If AI confirms: Status -> AI Cleared.

4. Final Review

Senior Admin reviews AI Cleared items for a one-click Final Approval.