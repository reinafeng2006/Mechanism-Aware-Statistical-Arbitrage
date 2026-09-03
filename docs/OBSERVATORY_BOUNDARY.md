# Observatory Import Boundary

Observatory is a separate, permanent hypothesis-discovery system.

## Allowed imports

Only discovery-context packets containing: observation text; Measurement Gaps; provisional hypotheses; source Observatory identifier; observation timestamp; export timestamp; and known limitations.

## Forbidden uses

An Observatory packet is not evidence, a label, a validated construct, literature coverage, a measurement specification, a feature-selection justification, an empirical result, or permission to inspect project outcomes. It cannot bypass independent construct definition, literature review, measurement design, timing audit, preregistration, development/held-out separation, or OOS validation.

## Quarantine workflow

1. Place the packet in a logically quarantined import manifest.
2. Assign an OI identifier and label it DISCOVERY CONTEXT ONLY.
3. Map each statement to a question, Measurement Gap, or provisional hypothesis.
4. Independently reconstruct definitions and source ancestry inside this project.
5. Route resulting proposals through the normal gate and decision registers.
6. Never cite the Observatory packet as support for a project claim.

## Import manifest schema

OI ID; Observatory source ID/version; exported-at; imported-at; importer; exact content hash; observation; Measurement Gap; provisional hypothesis; project question IDs; prohibited-use acknowledgement; independent follow-up status; reviewer.
