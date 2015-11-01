# Example

```
>>> from booksee import search
>>> results = search('legacy code')
>>> results
[Result(title='Working Effectively with Legacy Code', authors=['Michael Feathers']), Result(title='Working Effectively with Legacy Code', authors=['Michael Feathers']), Result(title='Addison Wesley - Perl Medic. Transforming Legacy Code.chm', authors=[''])]
>>> result = results[0]
>>> book = result.download()
>>> book.save()
>>> book.save('legacy-code.epub')
```
