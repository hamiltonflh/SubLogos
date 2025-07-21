


articles = [
    {
        "id" : '1',
        "title" : "Artigo 1",
        "content" : "Velit dolore duis eu do ad ut pariatur proident nisi tempor aliquip magna. Deserunt proident anim ex ex nostrud aliquip veniam quis. Labore deserunt ex dolore do nostrud labore ad in voluptate dolor. Minim nostrud consequat incididunt occaecat ex est culpa excepteur.",
        "resume" : "Sint excepteur veniam deserunt irure Lorem nulla sunt proident Lorem fugiat labore ut anim qui.",
        "destaque" : True
    },
    {
         "id" : '2',
        "title" : "Artigo 2",
        "content" : "Velit dolore duis eu do ad ut pariatur proident nisi tempor aliquip magna. Deserunt proident anim ex ex nostrud aliquip veniam quis. Labore deserunt ex dolore do nostrud labore ad in voluptate dolor. Minim nostrud consequat incididunt occaecat ex est culpa excepteur.",
        "resume" : "Sint excepteur veniam deserunt irure Lorem nulla sunt proident Lorem fugiat labore ut anim qui.",
        "destaque" : False
    },
    {
         "id" : '3',
        "title" : "Artigo 3",
        "content" : "Velit dolore duis eu do ad ut pariatur proident nisi tempor aliquip magna. Deserunt proident anim ex ex nostrud aliquip veniam quis. Labore deserunt ex dolore do nostrud labore ad in voluptate dolor. Minim nostrud consequat incididunt occaecat ex est culpa excepteur.",
        "resume" : "Sint excepteur veniam deserunt irure Lorem nulla sunt proident Lorem fugiat labore ut anim qui.",
        "destaque" : True
    },
    {
         "id" : '4',
        "title" : "Artigo 4",
        "content" : "Velit dolore duis eu do ad ut pariatur proident nisi tempor aliquip magna. Deserunt proident anim ex ex nostrud aliquip veniam quis. Labore deserunt ex dolore do nostrud labore ad in voluptate dolor. Minim nostrud consequat incididunt occaecat ex est culpa excepteur.",
        "resume" : "Sint excepteur veniam deserunt irure Lorem nulla sunt proident Lorem fugiat labore ut anim qui.",
        "destaque" : False
    },
    {
         "id" : '5',
        "title" : "Artigo 5",
        "content" : "Velit dolore duis eu do ad ut pariatur proident nisi tempor aliquip magna. Deserunt proident anim ex ex nostrud aliquip veniam quis. Labore deserunt ex dolore do nostrud labore ad in voluptate dolor. Minim nostrud consequat incididunt occaecat ex est culpa excepteur.",
        "resume" : "Sint excepteur veniam deserunt irure Lorem nulla sunt proident Lorem fugiat labore ut anim qui.",
        "destaque" : True
    },
    {
         "id" : '6',
        "title" : "Artigo 6",
        "content" : "Velit dolore duis eu do ad ut pariatur proident nisi tempor aliquip magna. Deserunt proident anim ex ex nostrud aliquip veniam quis. Labore deserunt ex dolore do nostrud labore ad in voluptate dolor. Minim nostrud consequat incididunt occaecat ex est culpa excepteur.",
        "resume" : "Sint excepteur veniam deserunt irure Lorem nulla sunt proident Lorem fugiat labore ut anim qui.",
        "destaque" : False
    }
]



destaques = list(filter(lambda artigo: artigo["destaque"], articles))