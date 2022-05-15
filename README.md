# Examinations.ie Scraper
I don't even need to use this website anymore as I've finished the LC but it pissed me off so much, so when I was looking for something to code I thought I might be able to improve it.

I have created a python flask webserver so now a website version of the
code can be run, which should be handier than using the command line.

You can access the scraper at https://examinations.eoin-cr.xyz/ .  It 
should be fully functional now (and in my opinion is nicer to use than
the examinations.ie website)

---

## Updated in this commit

Previously, there would only be a single url string that was kept track of in
the url scraper.  However, this would lead to issues when subjects had multiple
papers in one year for the same level and language.  To rectify this, I've
loaded the urls into an array instead, and now it works as expected.