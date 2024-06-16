# Actions
```sqlite
INSERT INTO Actions (ActionID, Person, Status, DueDate, CompletionDate, Notes, ItemID)
VALUES (...)
```

# Contains
```sqlite
INSERT INTO Contains (SubsystemID, ItemID)
VALUES (...)
```

# Hazardous Component
```sqlite
INSERT INTO HazardousComponent (ItemID, SubstanceName, PercentageComposition, RestrictionStatus)
VALUES (...)
```

# Restriction
```sqlite
INSERT INTO Restriction (Name, Threshold)
VALUES (...)
```

# Substance
```sqlite
INSERT INTO Substance (Name, SubstanceRestriction, Carcinogenicity)
VALUES (...)
```

# Subsystem
```sqlite
INSERT INTO Subsystem (Name)
VALUES (...)
```