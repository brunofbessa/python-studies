TESTS = {
    "allow_snake": "decorators_test.AllowSnakeTests",
    "count_calls": "decorators_test.CountCallsTests",
    "four": "decorators_test.FourTests",
    "groot": "decorators_test.GrootTests",
    "jsonify": "decorators_test.JSONifyTests",
    "overload": "decorators_test.OverloadTests",
    "positional_only": "decorators_test.PositionalOnlyTests",
    "record_calls": "decorators_test.RecordCallsTests",
    "alias": "descriptors_test.AliasTests",
    "class_only_method": "descriptors_test.ClassOnlyMethodTests",
    "class_property": "descriptors_test.ClassPropertyTests",
    "computed_property": "descriptors_test.ComputedPropertyTests",
    "RandomNumber": "descriptors_test.RandomNumberTests",
    "Hashable": "metaclasses_test.HashableTests",
    "InstanceTracker": "metaclasses_test.InstanceTrackerTests",
    "Mapping": "metaclasses_test.MappingTests",
    "NoMethodCollisions": "metaclasses_test.NoMethodCollisionsTests",
    "SnakeTestCase": "metaclasses_test.SnakeTestCaseTests",
    "UnsubclassableType": "metaclasses_test.UnsubclassableTypeTests"
}

MODULES = {
    "decorators": [
        "count_calls",
        "jsonify",
        "groot",
        "four",
        "record_calls",
        "positional_only",
        "allow_snake",
        "overload"
    ],
    "descriptors": [
        "RandomNumber",
        "alias",
        "class_property",
        "class_only_method",
        "computed_property"
    ],
    "metaclasses": [
        "UnsubclassableType",
        "InstanceTracker",
        "Mapping",
        "Hashable",
        "NoMethodCollisions",
        "SnakeTestCase"
    ]
}
