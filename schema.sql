CREATE TABLE IF NOT EXISTS "Subsystem" (
	"Name"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("Name")
);
CREATE TABLE IF NOT EXISTS "Item" (
	"ItemID"	TEXT NOT NULL UNIQUE,
	"Item Name"	TEXT,
	"Quantity"	INTEGER,
	"Category"	TEXT NOT NULL,
	"Hazard/Hazard Tracking System References"	TEXT,
	"Potential For Exposure"	TEXT,
	"Controls/Mitigations"	TEXT,
	"References"	TEXT,
	"Notes"	TEXT,
	PRIMARY KEY("ItemID")
);
CREATE TABLE IF NOT EXISTS "Restriction" (
	"RestrictionType"	TEXT NOT NULL UNIQUE,
	"Carcinogen Threshold"	TEXT NOT NULL,
	"Non-Carcinogen Threshold"	TEXT NOT NULL,
	PRIMARY KEY("RestrictionType")
);
CREATE TABLE IF NOT EXISTS "Substance" (
	"Name"	TEXT NOT NULL UNIQUE,
	"CAS Numbers"	TEXT,
	"Restriction"	TEXT NOT NULL,
	"Carcinogenicity"	TEXT NOT NULL CHECK("Carcinogenicity" = 'Carcinogen' OR "Carcinogenicity" = 'Non-Carcinogen'),
	FOREIGN KEY("Restriction") REFERENCES "Restriction"("RestrictionType") ON UPDATE CASCADE,
	PRIMARY KEY("Name")
);
CREATE TABLE IF NOT EXISTS "Contains" (
	"SubsystemName"	TEXT NOT NULL,
	"ItemID"	TEXT NOT NULL,
	FOREIGN KEY("SubsystemName") REFERENCES "Subsystem"("Name") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("ItemID") REFERENCES "Item"("ItemID") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("SubsystemName","ItemID")
);
CREATE TABLE IF NOT EXISTS "Actions" (
	"ActionID"	TEXT NOT NULL,
	"Person"	TEXT,
	"Status"	TEXT,
	"Due Date"	TEXT,
	"Completion Date"	TEXT,
	"Notes"	TEXT,
	"ItemID"	TEXT NOT NULL,
	FOREIGN KEY("ItemID") REFERENCES "Item"("ItemID") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("ActionID","ItemID")
);
CREATE TABLE IF NOT EXISTS "Hazardous Component" (
	"ItemID"	TEXT NOT NULL,
	"SubstanceName"	TEXT NOT NULL,
	"Weight Percentage"	TEXT NOT NULL,
	"Restriction Status"	TEXT,
	FOREIGN KEY("ItemID") REFERENCES "Item"("ItemID") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("SubstanceName") REFERENCES "Substance"("Name") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("ItemID","SubstanceName")
);
CREATE TABLE Users (
    username TEXT PRIMARY KEY,
    name TEXT,
    email TEXT,
    password TEXT,
    role TEXT
);
CREATE VIEW ActionReport AS
SELECT Item.ItemID, Item."Item Name", Actions.ActionID, Actions.Person AS "Personnel", Actions.Status, Actions."Due Date", Actions."Completion Date", Actions.Notes
FROM Actions
LEFT JOIN Item ON Item.ItemID = Actions.ItemID
ORDER BY Item.ItemID, Actions.ActionID
/* ActionReport(ItemID,"Item Name",ActionID,Personnel,Status,"Due Date","Completion Date",Notes) */;
CREATE VIEW FullReport AS
SELECT Item.ItemID, Item."Item Name", Item.Quantity, Subsystem.Name AS "Subsystem Name", Item.Category, Item."Hazard/Hazard Tracking System References", Item."Potential For Exposure", Item."Controls/Mitigations", Item."References", Item.Notes,  Substance.Name AS "Substance Name", Substance."CAS Numbers", Substance.Carcinogenicity, Restriction.RestrictionType AS "Restriction Type", Restriction."Carcinogen Threshold", Restriction."Non-Carcinogen Threshold", "Hazardous Component"."Weight Percentage", "Hazardous Component"."Restriction Status"
FROM Item
INNER JOIN "Hazardous Component" ON Item.ItemID = "Hazardous Component".ItemID
INNER JOIN Contains ON Contains.ItemID = Item.ItemID
LEFT JOIN Subsystem ON Subsystem.Name = Contains.SubsystemName
LEFT JOIN Substance ON "Hazardous Component".SubstanceName = Substance.Name
LEFT JOIN Restriction ON Restriction.RestrictionType = Substance.Restriction
ORDER BY Item.Category, Item."Item Name", Subsystem.Name, Substance.Name, Restriction.RestrictionType
/* FullReport(ItemID,"Item Name",Quantity,"Subsystem Name",Category,"Hazard/Hazard Tracking System References","Potential For Exposure","Controls/Mitigations","References",Notes,"Substance Name","CAS Numbers",Carcinogenicity,"Restriction Type","Carcinogen Threshold","Non-Carcinogen Threshold","Weight Percentage","Restriction Status") */;
CREATE VIEW HazMatReport AS
SELECT "Hazardous Component".ItemID, Item."Item Name", Substance.Name, Substance."CAS Numbers", Substance.Carcinogenicity, Restriction.RestrictionType, Restriction."Carcinogen Threshold", Restriction."Non-Carcinogen Threshold", "Hazardous Component"."Weight Percentage", "Hazardous Component"."Restriction Status"
FROM "Hazardous Component"
INNER JOIN Item ON Item.ItemID = "Hazardous Component".ItemID
INNER JOIN Substance ON "Hazardous Component".SubstanceName = Substance.Name
INNER JOIN Restriction ON Restriction.RestrictionType = Substance.Restriction
ORDER BY Item."Item Name", Substance.Name
/* HazMatReport(ItemID,"Item Name",Name,"CAS Numbers",Carcinogenicity,RestrictionType,"Carcinogen Threshold","Non-Carcinogen Threshold","Weight Percentage","Restriction Status") */;
CREATE VIEW HazardReport AS
SELECT Item.ItemID, Item."Item Name", Item."Hazard/Hazard Tracking System References"
FROM Item
ORDER BY Item."Item Name"
/* HazardReport(ItemID,"Item Name","Hazard/Hazard Tracking System References") */;
