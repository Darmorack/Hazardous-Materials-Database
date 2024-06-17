# Item
```sqlite
INSERT INTO Item ('ItemID', 'Item Name', 'Quantity', 'Category', 'Hazard/Hazard Tracking System References', 'Potential For Exposure', 'Controls/Mitigations', 'References', 'Notes')
VALUES (item_id, item_name, quantity, category, hazard_tracking_system_references, potential_for_exposure, controls_mitigations, references, notes

# Actions
```sqlite
INSERT INTO Actions ('ActionID', 'Person', 'Status', 'Due Date', 'Completion Date', 'Notes', 'ItemID')
VALUES (action_id, person, status, due_date, completion_date, notes, item_id)
```

# Contains
```sqlite
INSERT INTO Contains ('SubsystemName', 'ItemID')
VALUES (subsystem_name, item_id)
```

# Hazardous Component
```sqlite
INSERT INTO HazardousComponent ('ItemID', 'SubstanceName', 'Weight Percentage', 'Restriction Status')
VALUES (item_id, subsystem_name)
```

# Restriction
```sqlite
INSERT INTO Restriction ('Name', 'Carcinogen Threshold', Non-Carcinogen Threshold)
VALUES (restriction_name, carcinogen_threshold, non_carcinogen_threshold)
```

# Substance
```sqlite
INSERT INTO Substance ('Name', 'CAS Numbers', 'Carcinogenicity')
VALUES (substance_name, casnumbers, carcinogenicity)
```

# Subsystem
```sqlite
INSERT INTO Subsystem (Name)
VALUES (subsystem_name)
```
