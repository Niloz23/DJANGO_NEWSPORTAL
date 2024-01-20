from django import template


register = template.Library()


undesirable_words = ['нежелательное_слово1', 'нежелательное_слово5', 'нежелательное_слово2']
@register.filter()
def censor(value):
   for word in undesirable_words:
      value = value.replace(word, '*' * len(word), -1)
   return value