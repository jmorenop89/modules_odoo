{
    'name' : 'Add a report to print a partner card',

    'summary' : """
        Adds a printed report for the partners
    """,

    'description' : """
        Adds a Qweb report into tehe res.partner model.
    """,

    'author' : "JMP",

    'website' : "http://www.janaq.com",

    'category' : 'Customization',

    'version' : '0.1',

    'depends' : ['base'],

    'data' : [
        #'security/ir.model.access.csv',
        'reports/report_partner.xml',
        #'views/data'
    ],
    'demo': [
        # 'demo/demo.xml'
    ],
}