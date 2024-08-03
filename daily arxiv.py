#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import arxiv

search = arxiv.Search(
  max_results=10,
  sort_by=arxiv.SortCriterion.SubmittedDate,
  query = "cat:q-fin.PM"

)

for result in search.results():
    
  print(result.entry_id, '->', result.title,'->',result.primary_category,'->',result.updated)

