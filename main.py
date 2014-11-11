# coding: utf-8
import SnippetGetter as Snip


snippets = Snip.get_ameba(["ざあざあ"])
for snippet in snippets:
  print(snippet)

