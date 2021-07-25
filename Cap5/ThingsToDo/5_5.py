letter = {
'salutation':'especial',
'name' : 'Pedro',
'product' : 'motor',
'verbed' : 'worked',
'room' : 'kitchen',
'animals' : 'dogs',
'amount' : '50 dollars',
'percent' : '100',
'spokesman' : 'Jorge Quiroz',
'job_tittle' : 'Manager General'
}
print("""Dear {0[salutation]} {0[name]} ,
Thank for your letter. We are sorry that our {0[product]}
{0[verbed]} in your {0[room]}. Please note that it should never
be used in a {0[room]} , especially near any {0[animals]}.

Send us your receipt and {0[amount]} for shipping and handling.
We will send you another {0[product]} that, in our tests,
is {0[percent]} less likely to have {0[verbed]}.

Thank you for you support.

Sincerely,
{0[spokesman]}
{0[job_tittle]}""".format(letter))