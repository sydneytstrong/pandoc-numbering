# This Python file uses the following encoding: utf-8

from unittest import TestCase

from helper import verify_conversion


class ListingsTest(TestCase):
    def test_listing_classic(self):
        verify_conversion(
            self,
            r"""
---
pandoc-numbering:
  exercise:
    general:
      listing-title: List of exercises
---

Exercise #

Exercise (Title) #
            """,
            r"""
---
pandoc-numbering:
  exercise:
    general:
      listing-title: List of exercises
---

List of exercises {#list-of-exercises .pandoc-numbering-listing .exercise .unnumbered .unlisted}
=================

-   [[Exercise 1]{.pandoc-numbering-entry .exercise}](#exercise:1)
-   [[Title]{.pandoc-numbering-entry .exercise}](#exercise:2)

[**Exercise 1**]{#exercise:1 .pandoc-numbering-text .exercise}

[**Exercise 2** *(Title)*]{#exercise:2 .pandoc-numbering-text .exercise}
            """,
        )

    def test_listing_identifier_false(self):
        verify_conversion(
            self,
            r"""
---
pandoc-numbering:
  exercise:
    general:
      listing-identifier: False
      listing-title: List of exercises
---

Exercise #

Exercise (Title) #
            """,
            r"""
---
pandoc-numbering:
  exercise:
    general:
      listing-title: List of exercises
---

List of exercises {.pandoc-numbering-listing .exercise .unnumbered .unlisted}
=================

-   [[Exercise 1]{.pandoc-numbering-entry .exercise}](#exercise:1)
-   [[Title]{.pandoc-numbering-entry .exercise}](#exercise:2)

[**Exercise 1**]{#exercise:1 .pandoc-numbering-text .exercise}

[**Exercise 2** *(Title)*]{#exercise:2 .pandoc-numbering-text .exercise}
            """,
        )

    def test_listing_identifier(self):
        verify_conversion(
            self,
            r"""
---
pandoc-numbering:
  exercise:
    general:
      listing-identifier: myident
      listing-title: List of exercises
---

Exercise #

Exercise (Title) #
            """,
            r"""
---
pandoc-numbering:
  exercise:
    general:
      listing-identifier: myident
      listing-title: List of exercises
---

List of exercises {#myident .pandoc-numbering-listing .exercise .unnumbered .unlisted}
=================

-   [[Exercise 1]{.pandoc-numbering-entry .exercise}](#exercise:1)
-   [[Title]{.pandoc-numbering-entry .exercise}](#exercise:2)

[**Exercise 1**]{#exercise:1 .pandoc-numbering-text .exercise}

[**Exercise 2** *(Title)*]{#exercise:2 .pandoc-numbering-text .exercise}
            """,
        )

    def test_listing_options(self):
        verify_conversion(
            self,
            r"""
---
pandoc-numbering:
  exercise:
    general:
      listing-title: List of exercises
      listing-unlisted: False
      listing-unnumbered: False
---

Exercise #

Exercise (Title) #
            """,
            r"""
---
pandoc-numbering:
  exercise:
    general:
      listing-title: List of exercises
---

List of exercises {#list-of-exercises .pandoc-numbering-listing .exercise}
=================

-   [[Exercise 1]{.pandoc-numbering-entry .exercise}](#exercise:1)
-   [[Title]{.pandoc-numbering-entry .exercise}](#exercise:2)

[**Exercise 1**]{#exercise:1 .pandoc-numbering-text .exercise}

[**Exercise 2** *(Title)*]{#exercise:2 .pandoc-numbering-text .exercise}
            """,
        )

    def test_listing_latex(self):
        verify_conversion(
            self,
            r"""
---
pandoc-numbering:
  exercise:
    general:
      listing-title: List of exercises
---

Exercise #

Exercise (Title) #
            """,
            r"""
---
pandoc-numbering:
  exercise:
    general:
      listing-title: List of exercises
---

List of exercises {#list-of-exercises .pandoc-numbering-listing .exercise .unnumbered .unlisted}
=================

```{=tex}
\hypersetup{linkcolor=black}\makeatletter\newcommand*\l@exercise{\@dottedtocline{1}{1.5em}{2.3em}}\@starttoc{exercise}\makeatother
```
`\phantomsection\addcontentsline{exercise}{exercise}{\protect\numberline {1}{\ignorespaces {Exercise}}}`{=tex}[`\label{exercise:1}`{=tex}**Exercise 1**]{#exercise:1 .pandoc-numbering-text .exercise}

`\phantomsection\addcontentsline{exercise}{exercise}{\protect\numberline {2}{\ignorespaces {Title}}}`{=tex}[`\label{exercise:2}`{=tex}**Exercise 2** *(Title)*]{#exercise:2 .pandoc-numbering-text .exercise}
            """,
            "latex",
        )

    def test_listing_classic_format(self):
        verify_conversion(
            self,
            r"""
---
pandoc-numbering:
  exercise:
    general:
      listing-title: List of exercises
    standard:
      format-entry-classic: '%g %D'
      format-entry-title: '%g %D (%T)'
---

Exercise #

Exercise (Title) #
            """,
            r"""
---
pandoc-numbering:
  exercise:
    general:
      listing-title: List of exercises
    standard:
      format-entry-classic: '%g %D'
      format-entry-title: '%g %D (%T)'
---

List of exercises {#list-of-exercises .pandoc-numbering-listing .exercise .unnumbered .unlisted}
=================

-   [[1 Exercise]{.pandoc-numbering-entry .exercise}](#exercise:1)
-   [[2 Exercise (Title)]{.pandoc-numbering-entry .exercise}](#exercise:2)

[**Exercise 1**]{#exercise:1 .pandoc-numbering-text .exercise}

[**Exercise 2** *(Title)*]{#exercise:2 .pandoc-numbering-text .exercise}
            """,
        )

    def test_listing_latex_format(self):
        verify_conversion(
            self,
            r"""
---
pandoc-numbering:
  exercise:
    general:
      listing-title: List of exercises
    latex:
      entry-space: 3
      entry-tab: 2
      format-entry-classic: '%D'
      format-entry-title: '%D (%T)'
toccolor: blue
---

Exercise #

Exercise (Title) #
            """,
            r"""
---
pandoc-numbering:
  exercise:
    general:
      listing-title: List of exercises
    latex:
      entry-space: 3
      entry-tab: 2
      format-entry-classic: '%D'
      format-entry-title: '%D (%T)'
toccolor: blue
---

List of exercises {#list-of-exercises .pandoc-numbering-listing .exercise .unnumbered .unlisted}
=================

```{=tex}
\hypersetup{linkcolor=blue}\makeatletter\newcommand*\l@exercise{\@dottedtocline{1}{2.0em}{3.0em}}\@starttoc{exercise}\makeatother
```
`\phantomsection\addcontentsline{exercise}{exercise}{\protect\numberline {1}{\ignorespaces {Exercise}}}`{=tex}[`\label{exercise:1}`{=tex}**Exercise 1**]{#exercise:1 .pandoc-numbering-text .exercise}

`\phantomsection\addcontentsline{exercise}{exercise}{\protect\numberline {2}{\ignorespaces {Exercise (Title)}}}`{=tex}[`\label{exercise:2}`{=tex}**Exercise 2** *(Title)*]{#exercise:2 .pandoc-numbering-text .exercise}
            """,
            "latex",
        )
