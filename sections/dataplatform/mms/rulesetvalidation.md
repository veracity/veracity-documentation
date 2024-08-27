---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# Rulesets
Ruleset can be defined as a set of rules. Rulesets are defined as part of the standard.
Rulesets are used to validate a site

## Add ruleset
Provide ruleset-name and a description. Ruleset-name must be unique.

## Add rule
Each ruleset contains a list of rules.

Each rule has a type; the following types are supported (more can be developed):
- NotNull: Verifies if a parameter exist or a metadata is defined with value
- WithinRange: Verify that metadata value is within min and max (if defined)

When adding a rule, define which asset model type it will validate. One rule per asset model type

# Example

For all inverters, validate that metadata CapacityAC and CapacityDC is defined (with value) and that Parameter CurrentDC is defined as operational data.
For site level, verify thar AkkiwStuck is within the allowed range.
```
{
  "ruleset": "Example",
  "description": "Inverter and Meter validation",
  "rules": [
    {
      "type": "NotNull",
      "assetModel": "Inverter",
      "metadata": [
        "CapacityAC",
        "CapacityDC"
      ],
      "parameters": [
        "CurrentDC"
      ]
    }
    ....  (new rule for each device type)
  ]
}
```

### API
Base url: https://api.veracity.com/veracity/mms/schema/

Explore the api [Asset Model Standard](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/DataFabric-MMS-Schema-API-swagger.json). 

