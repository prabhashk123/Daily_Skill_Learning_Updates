# step1
from django import template
register=template.Library()

# def evenUpper(value):
#     return "Hello"
# # step 2 register filter method jo ki name oe method lega
# register.filter('EvenUpper',evenUpper)
def evenUpper(value):
    data=""
    for i in range(len(value)):
        ch=value[i]
        code=ord(ch)
        if i%2==0:
            if(code>=97 and code<=122):
                code-=32
        else:
            if(code>=65 and code<=97):
                code+=32
        data+=chr(code)
    return data
# replace string with filter
@register.filter(name='spacefilter')
def spacereplaceString(value,s):
    return value.replace(' ',s)

register.filter('EvenUpper',evenUpper)



