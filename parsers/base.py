from abc import ABC, abstractmethod


class Parser(ABC):
    """
    Base class for all COVIDScholar parsers. Please implement your parser against this API
    and inherit from this base class.

    Every parser should make its best effort to get a value for each of the following fields,
    either from the original document that is being parsed or by calling an external API that can
    supply that information. If data for a field doesn't exist for a paper (e.g. a PubMed ID
    for a paper is not on PubMed), then return None.
    """

    keys = [
        "doi",
        "title",
        "authors",
        "journal",
        "journal_short",
        "publication_date",
        "abstract",
        "origin",
        "source_display",
        "last_updated",
        "body_text",
        "has_full_text",
        "references",
        "cited_by",
        "link",
        "category_human",
        "keywords",
        "summary_human",
        "has_year",
        "has_month",
        "has_day",
        "is_pre_proof",
        "is_covid19",
        "license",
        "cord_uid",
        "pmcid",
        "pubmed_id",
        "who_covidence",
    ]

    @abstractmethod
    def _parse_doi(self, doc):
        """ Returns the DOI of a document as a <class 'str'>"""
        pass

    @abstractmethod
    def _parse_title(self, doc):
        """ Returns the title of a document as a <class 'str'>"""
        pass

    @abstractmethod
    def _parse_authors(self, doc):
        """ Returns the authors of a document as a <class 'list'> of <class 'dict'>.
        Each element in the authors list should have a "name" field with the author's
        full name (e.g. John Smith or J. Smith) as a <class 'str'>. Feel free to include
        any other fields you have under other field names. Suggested fields are: "first_name",
        "middle_name", "last_name", "institution", "email".
        """
        pass

    @abstractmethod
    def _parse_journal(self, doc):
        """ Returns the journal of a document as a <class 'str'>. """
        pass

    @abstractmethod
    def _parse_journal_short(self, doc):
        """ Returns the shortend journal name of a document as a <class 'str'>, if available.
         e.g. 'Comp. Mat. Sci.' """
        pass

    @abstractmethod
    def _parse_issn(self, doc):
        """ Returns the ISSN and (or) EISSN for the journal of a document as a
        <class 'list'> of <class 'str'> """

    @abstractmethod
    def _parse_publication_date(self, doc):
        """ Returns the publication_date of a document as a <class 'datetime.datetime'>"""
        pass

    # def _parse_timestamp(self, doc):
    #     """ Returns the POSIX timestamp of a document as a <class 'int'>.
    #
    #     You can get this with datetime.timestamp()
    #
    #     """
    #     pass

    @abstractmethod
    def _parse_abstract(self, doc):
        """ Returns the abstract of a document as a <class 'str'>"""
        pass

    @abstractmethod
    def _parse_origin(self, doc):
        """ Returns the origin of the document as a <class 'str'>. Use the mongodb collection
        name for this."""
        pass

    @abstractmethod
    def _parse_source_display(self, doc):
        """ Returns the source of the document as a <class 'str'>. This is what will be
        displayed on the website, so use something people will recognize properly and
        use proper capitalization."""
        pass

    @abstractmethod
    def _parse_last_updated(self, doc):
        """ Returns when the entry was last_updated as a <class 'datetime.datetime'>. Note
        this should probably not be the _bt field in a Parser."""
        pass

    @abstractmethod
    def _parse_has_full_text(self, doc):
        """ Returns a <class 'bool'> specifying if we have the full text."""
        pass

    @abstractmethod
    def _parse_body_text(self, doc):
        """ Returns the body_text of a document as a <class 'list'> of <class 'dict'>.
        This should be a list of objects of some kind. Seems to be usually something like
        {'section_heading':  <class 'str'>,
         'text': <class 'str'>
         }

         """
        pass

    @abstractmethod
    def _parse_references(self, doc):
        """ Returns the references of a document as a <class 'list'> of <class 'dict'>.
        This is a list of documents cited by the current document. Try to include "doi"
        as a field for each reference if at all possible.
        """
        pass

    @abstractmethod
    def _parse_cited_by(self, doc):
        """ Returns the citations of a document as a <class 'list'> of <class 'dict'>.
        A list of documents that cite this document. Try to include "doi"
        as a field for each citation if at all possible.
        """
        pass

    @abstractmethod
    def _parse_link(self, doc):
        """ Returns the url of a document as a <class 'str'>"""
        pass

    @abstractmethod
    def _parse_category_human(self, doc):
        """ Returns the category_human of a document as a <class 'list'> of <class 'str'>"""
        pass

    @abstractmethod
    def _parse_keywords(self, doc):
        """ Returns the keywords for a document from original source as a a <class 'list'> of <class 'str'>"""
        pass

    @abstractmethod
    def _parse_summary_human(self, doc):
        """ Returns the human-written summary of a document as a <class 'list'> of <class 'str'>"""
        pass

    @abstractmethod
    def _parse_has_year(self, doc):
        """ Returns a <class 'bool'> specifying whether a document's year can be trusted."""
        pass

    @abstractmethod
    def _parse_has_month(self, doc):
        """ Returns a <class 'bool'> specifying whether a document's month can be trusted."""
        pass

    @abstractmethod
    def _parse_has_day(self, doc):
        """ Returns a <class 'bool'> specifying whether a document's day can be trusted."""
        pass

    @abstractmethod
    def _parse_is_preprint(self, doc):
        """ Returns a <class 'bool'> specifying whether the document is a preprint.
        If it's not immediately clear from the source it's coming from, return None."""
        pass

    @abstractmethod
    def _parse_is_covid19(self, doc):
        """ Returns a <class 'bool'> if we know for sure a document is specifically about COVID-19.
        If it's not immediately clear from the source it's coming from, return None."""
        pass

    @abstractmethod
    def _parse_license(self, doc):
        """ Returns the license of a document as a <class 'str'> if it is specified in the original doc."""
        pass

    @abstractmethod
    def _parse_pmcid(self, doc):
        """ Returns the pmcid of a document as a <class 'str'>."""
        pass

    @abstractmethod
    def _parse_pubmed_id(self, doc):
        """ Returns the PubMed ID of a document as a <class 'str'>."""
        pass

    @abstractmethod
    def _parse_who_covidence(self, doc):
        """ Returns the who_covidence of a document as a <class 'str'>."""
        pass

    @abstractmethod
    def _parse_version(self, doc):
        """ Returns the version of a document as a <class 'int'>."""
        pass

    @abstractmethod
    def _parse_copyright(self, doc):
        """ Returns the copyright notice of a document as a <class 'str'>."""
        pass


    def _preprocess(self, doc):
        """ Do any preprocessing you need in this method. doc=self._preprocess(doc)
        is called before the doc is parsed by the various _parse_<field> methods
        are called to construct the parsed doc."""
        return doc

    def _postprocess(self, doc, parsed_doc):
        """
        Post-process an entry to add any last-minute fields required.

        """
        return parsed_doc

    def parse(self, doc):
        """
        Parses the input document into the standardized COVIDScholar entry format.
        Do not overwrite this method with your own 'parse' method!

        Args:
            doc: Whatever your input object is.

        Returns:

            (dict) Parsed entry.

        """
        doc = self._preprocess(doc)

        return self._postprocess(doc,
                                 {
                                     "doi": self._parse_doi(doc),
                                     "title": self._parse_title(doc),
                                     "authors": self._parse_authors(doc),
                                     "journal": self._parse_journal(doc),
                                     "journal_short": self._parse_journal_short(doc),
                                     "issn": self._parse_issn(doc),
                                     "publication_date": self._parse_publication_date(doc),
                                     "abstract": self._parse_abstract(doc),
                                     "origin": self._parse_origin(doc),
                                     "source_display": self._parse_source_display(doc),
                                     "last_updated": self._parse_last_updated(doc),
                                     "body_text": self._parse_body_text(doc),
                                     "has_full_text": self._parse_has_full_text(doc),
                                     "references": self._parse_references(doc),
                                     "cited_by": self._parse_cited_by(doc),
                                     "link": self._parse_link(doc),
                                     "category_human": self._parse_category_human(doc),
                                     "keywords": self._parse_keywords(doc),
                                     "summary_human": self._parse_summary_human(doc),
                                     "has_year": self._parse_has_year(doc),
                                     "has_month": self._parse_has_month(doc),
                                     "has_day": self._parse_has_day(doc),
                                     "is_preprint": self._parse_is_preprint(doc),
                                     "is_covid19": self._parse_is_covid19(doc),
                                     "license": self._parse_license(doc),
                                     "pmcid": self._parse_pmcid(doc),
                                     "pubmed_id": self._parse_pubmed_id(doc),
                                     "who_covidence": self._parse_who_covidence(doc),
                                     "version": self._parse_version(doc)
                                 }
                                 )
