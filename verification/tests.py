"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[1,2,3,4]],
            "answer": [2,1,4,3]
        },
        {
            "input": [[5,5,5,5]],
            "answer": [5,5,5,5]
        },
        {
            "input": [[1,2,3]],
            "answer": [2,1,3]
        },
        {
            "input": [[3]],
            "answer": [3]
        },
        {
            "input": [['hello', 'world']],
            "answer": ['world', 'hello']
        },
        {
            "input": [[]],
            "answer": []
        }
    ],
    "Extra": [
        {
            "input": [[7, 10, 80, 12]],
            "answer": [10, 7, 12, 80]
        },
        {
            "input": [[3,3,5,5,8]],
            "answer": [3,3,5,5,8]
        }
    ]
}
