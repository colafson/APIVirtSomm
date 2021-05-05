import pickle 
# a standard python library
# pickle (AKA object serialization): writing a binary representation of an object to a file
# unpickle (AKA object de-serialization): read a binary representation of an object from a file
# to load a python object in to memory


# for the project... imagine this is a MyRandomForestClassifier
# for PA6... imagine this is a MyDecisionTreeClassifier
# both of which were just trained with fit()
#header = ["level", "lang", "tweets", "phd"]
"""
interview_tree = \
["Attribute", "level", 
    ["Value", "Senior", 
        ["Attribute", "tweets", 
            ["Value", "yes", 
                ["Leaf", "True", 2, 5]
            ],
            ["Value", "no", 
                ["Leaf", "False", 3, 5]
            ]
        ]
    ],
    ["Value", "Mid", 
        ["Leaf", "True", 4, 14]
    ],
    ["Value", "Junior", 
        ["Attribute", "phd", 
            ["Value", "yes", 
                ["Leaf", "False", 2, 5]
            ],
            ["Value", "no", 
                ["Leaf", "True", 3, 5]
            ]
        ]
    ]
]
"""

header = ["country", "province", "price", "variety"]


virt_somm_tree = ['Attribute', 'price', ['Value', 13.0, ['Leaf', 87.0, 49, 200]], ['Value', 40.0, ['Leaf', 89.0, 32, 211]], ['Value', 56.0, ['Leaf', 90.0, 4, 16]], ['Value', 17.0, ['Leaf', 87.0, 39, 181]], ['Value', 48.0, ['Leaf', 90.0, 16, 95]], ['Value', 34.0, ['Leaf', 92.0, 14, 62]], ['Value', 14.0, ['Leaf', 87.0, 30, 153]], ['Value', 36.0, ['Leaf', 89.0, 14, 65]], ['Value', 65.0, ['Leaf', 90.0, 18, 108]], ['Value', 38.0, ['Leaf', 90.0, 16, 94]], ['Value', 28.0, ['Leaf', 88.0, 35, 158]], ['Value', 22.0, ['Leaf', 89.0, 35, 190]], ['Value', 60.0, ['Leaf', 90.0, 21, 124]], ['Value', 18.0, ['Leaf', 88.0, 67, 272]], ['Value', 16.0, ['Leaf', 88.0, 42, 190]], ['Value', 20.0, ['Leaf', 88.0, 88, 381]], ['Value', 15.0, ['Leaf', 87.0, 61, 288]], ['Value', 23.0, ['Leaf', 88.0, 21, 109]], ['Value', '', ['Leaf', 88.0, 65, 353]], ['Value', 21.0, ['Leaf', 88.0, 15, 65]], ['Value', 105.0, ['Leaf', 94.0, 3, 6]], ['Value', 70.0, ['Leaf', 90.0, 9, 46]], ['Value', 8.0, ['Leaf', 86.0, 10, 31]], ['Value', 45.0, ['Leaf', 89.0, 27, 150]], ['Value', 10.0, ['Leaf', 86.0, 40, 141]], ['Value', 55.0, ['Leaf', 90.0, 19, 91]], ['Value', 12.0, ['Leaf', 86.0, 35, 173]], ['Value', 35.0, ['Leaf', 90.0, 39, 187]], ['Value', 32.0, ['Leaf', 90.0, 17, 111]], ['Value', 26.0, ['Leaf', 90.0, 22, 111]], ['Value', 62.0, ['Leaf', 92.0, 3, 12]], ['Value', 25.0, ['Leaf', 88.0, 92, 347]], ['Value', 49.0, ['Leaf', 92.0, 10, 30]], ['Value', 9.0, ['Leaf', 85.0, 17, 54]], ['Value', 11.0, ['Leaf', 87.0, 22, 84]], ['Value', 24.0, ['Leaf', 88.0, 32, 157]], ['Value', 30.0, ['Leaf', 88.0, 56, 267]], ['Value', 80.0, ['Leaf', 92.0, 10, 45]], ['Value', 75.0, ['Leaf', 90.0, 14, 55]], ['Value', 33.0, ['Leaf', 90.0, 8, 35]], ['Value', 42.0, ['Leaf', 90.0, 27, 90]], ['Value', 7.0, ['Leaf', 86.0, 6, 17]], ['Value', 85.0, ['Leaf', 93.0, 7, 34]], ['Value', 43.0, ['Leaf', 92.0, 5, 16]], ['Value', 350.0, ['Leaf', 94.0, 1, 6699]], ['Value', 50.0, ['Leaf', 90.0, 29, 159]], ['Value', 19.0, ['Leaf', 88.0, 44, 142]], ['Value', 90.0, ['Leaf', 92.0, 6, 48]], ['Value', 86.0, ['Leaf', 95.0, 1, 6699]], ['Value', 53.0, ['Leaf', 92.0, 3, 10]], ['Value', 125.0, ['Leaf', 92.0, 5, 16]], ['Value', 120.0, ['Leaf', 93.0, 4, 17]], ['Value', 95.0, ['Leaf', 90.0, 6, 21]], ['Value', 27.0, ['Leaf', 89.0, 15, 74]], ['Value', 39.0, ['Leaf', 89.0, 10, 46]], ['Value', 52.0, ['Leaf', 90.0, 4, 17]], ['Value', 29.0, ['Leaf', 88.0, 14, 69]], ['Value', 37.0, ['Leaf', 88.0, 7, 27]], ['Value', 294.0, ['Leaf', 94.0, 1, 6699]], ['Value', 200.0, ['Leaf', 95.0, 1, 4]], ['Value', 44.0, ['Leaf', 90.0, 9, 38]], ['Value', 63.0, ['Leaf', 92.0, 4, 16]], ['Value', 57.0, ['Leaf', 87.0, 2, 8]], ['Value', 59.0, ['Leaf', 92.0, 5, 19]], ['Value', 64.0, ['Leaf', 91.0, 4, 12]], ['Value', 54.0, ['Leaf', 92.0, 7, 23]], ['Value', 100.0, ['Leaf', 93.0, 7, 32]], ['Value', 115.0, ['Leaf', 91.0, 1, 3]], ['Value', 300.0, ['Leaf', 94.0, 1, 2]], ['Value', 66.0, ['Leaf', 90.0, 3, 11]], ['Value', 72.0, ['Leaf', 88.0, 4, 11]], ['Value', 77.0, ['Leaf', 92.0, 1, 2]], ['Value', 150.0, ['Leaf', 94.0, 2, 9]], ['Value', 58.0, ['Leaf', 93.0, 5, 22]], ['Value', 46.0, ['Leaf', 88.0, 6, 33]], ['Value', 61.0, ['Leaf', 92.0, 2, 5]], ['Value', 47.0, ['Leaf', 89.0, 3, 5]], ['Value', 94.0, ['Leaf', 92.0, 1, 3]], ['Value', 110.0, ['Leaf', 93.0, 2, 9]], ['Value', 99.0, ['Leaf', 88.0, 1, 4]], ['Value', 141.0, ['Leaf', 90.0, 1, 6699]], ['Value', 140.0, ['Leaf', 94.0, 3, 8]], ['Value', 31.0, ['Leaf', 89.0, 3, 12]], ['Value', 152.0, ['Leaf', 93.0, 1, 6699]], ['Value', 119.0, ['Leaf', 89.0, 1, 6699]], ['Value', 135.0, ['Leaf', 90.0, 3, 6]], ['Value', 51.0, ['Leaf', 93.0, 2, 4]], ['Value', 92.0, ['Leaf', 92.0, 3, 4]], ['Value', 365.0, ['Leaf', 93.0, 1, 2]], ['Value', 74.0, ['Leaf', 90.0, 2, 5]], ['Value', 240.0, ['Leaf', 96.0, 1, 2]], ['Value', 88.0, ['Leaf', 89.0, 2, 4]], ['Value', 130.0, ['Leaf', 94.0, 2, 5]], ['Value', 187.0, ['Leaf', 95.0, 1, 6699]], ['Value', 185.0, ['Leaf', 94.0, 1, 2]], ['Value', 770.0, ['Leaf', 96.0, 1, 6699]], ['Value', 79.0, ['Leaf', 89.0, 3, 5]], ['Value', 83.0, ['Leaf', 95.0, 1, 2]], ['Value', 6.0, ['Leaf', 87.0, 1, 6699]], ['Value', 82.0, ['Leaf', 95.0, 2, 6]], ['Value', 257.0, ['Leaf', 94.0, 1, 6699]], ['Value', 5.0, ['Leaf', 81.0, 1, 6699]], ['Value', 68.0, ['Leaf', 94.0, 4, 13]], ['Value', 280.0, ['Leaf', 93.0, 1, 6699]], ['Value', 179.0, ['Leaf', 94.0, 1, 6699]], ['Value', 136.0, ['Leaf', 93.0, 1, 6699]], ['Value', 235.0, ['Leaf', 96.0, 1, 2]], ['Value', 202.0, ['Leaf', 95.0, 1, 6699]], ['Value', 225.0, ['Leaf', 95.0, 1, 2]], ['Value', 698.0, ['Leaf', 97.0, 1, 6699]], ['Value', 113.0, ['Leaf', 92.0, 1, 6699]], ['Value', 124.0, ['Leaf', 88.0, 1, 6699]], ['Value', 103.0, ['Leaf', 90.0, 2, 3]], ['Value', 325.0, ['Leaf', 87.0, 1, 6699]], ['Value', 98.0, ['Leaf', 94.0, 1, 5]], ['Value', 76.0, ['Leaf', 89.0, 1, 2]], ['Value', 450.0, ['Leaf', 97.0, 1, 2]], ['Value', 137.0, ['Leaf', 90.0, 1, 6699]], ['Value', 93.0, ['Leaf', 91.0, 1, 3]], ['Value', 73.0, ['Leaf', 95.0, 1, 2]], ['Value', 282.0, ['Leaf', 93.0, 1, 6699]], ['Value', 96.0, ['Leaf', 88.0, 1, 2]], ['Value', 500.0, ['Leaf', 89.0, 1, 2]], ['Value', 220.0, ['Leaf', 95.0, 1, 6699]], ['Value', 78.0, ['Leaf', 93.0, 2, 5]], ['Value', 41.0, ['Leaf', 90.0, 3, 7]], ['Value', 69.0, ['Leaf', 90.0, 1, 3]], ['Value', 195.0, ['Leaf', 89.0, 1, 2]], ['Value', 391.0, ['Leaf', 93.0, 1, 6699]], ['Value', 145.0, ['Leaf', 92.0, 1, 6699]], ['Value', 108.0, ['Leaf', 93.0, 1, 6699]], ['Value', 107.0, ['Leaf', 89.0, 1, 6699]], ['Value', 67.0, ['Leaf', 91.0, 1, 3]], ['Value', 160.0, ['Leaf', 96.0, 1, 6699]], ['Value', 97.0, ['Leaf', 94.0, 1, 2]], ['Value', 165.0, ['Leaf', 87.0, 1, 6699]], ['Value', 118.0, ['Leaf', 92.0, 1, 6699]], ['Value', 238.0, ['Leaf', 90.0, 1, 6699]], ['Value', 89.0, ['Leaf', 94.0, 1, 2]], ['Value', 175.0, ['Leaf', 91.0, 2, 3]], ['Value', 848.0, ['Leaf', 100.0, 1, 6699]], ['Value', 138.0, ['Leaf', 87.0, 1, 6699]], ['Value', 128.0, ['Leaf', 89.0, 1, 6699]], ['Value', 149.0, ['Leaf', 92.0, 1, 6699]], ['Value', 180.0, ['Leaf', 95.0, 1, 6699]], ['Value', 102.0, ['Leaf', 93.0, 1, 6699]], ['Value', 250.0, ['Leaf', 89.0, 1, 2]], ['Value', 111.0, ['Leaf', 90.0, 1, 6699]], ['Value', 740.0, ['Leaf', 93.0, 1, 6699]], ['Value', 117.0, ['Leaf', 90.0, 1, 6699]], ['Value', 156.0, ['Leaf', 92.0, 1, 6699]], ['Value', 84.0, ['Leaf', 93.0, 1, 6699]], ['Value', 129.0, ['Leaf', 90.0, 1, 6699]], ['Value', 91.0, ['Leaf', 93.0, 1, 6699]]]

# pickle (save to file) header and interview tree as one object
packaged_object = [header, virt_somm_tree]
outfile = open("tree.p", "wb")
pickle.dump(packaged_object, outfile)
outfile.close()
