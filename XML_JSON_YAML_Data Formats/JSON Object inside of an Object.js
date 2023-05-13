Obj = {"student" : [
    {
        "ID" :1 ,
        "Name" : {"FN": "Medi", "LN" : "Amiri"},
        "Birthdate" : "04.04.1369",
        "Active" : true
    },
    {
        "ID" : "2",
        "Name" : {"FN": "Medi2", "LN" : "Amiri2"},
        "Birthdate" : "05.05.1369",
        "Active" : false
    },
    {
        "ID" : "3",
        "Name" : {"FN": "Medi3", "LN" : "Amiri3"},
        "Birthdate" : "06.06.1369",
        "Active" : false
    }
]
} 

console.log(Obj.student[2].Name.FN)