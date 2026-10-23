Currently bleve fields can have more then one value, especially if we're indexing an array. In this cases the range facet (numeric and datetime) count the values, not the documents. Term facets on a field the mapping declares as a number or a date are even worse, they return the raw encoded index terms, several per value.

Range facets should count documents, where each nested object counts as its own document just like in term facets. A document counts once in each range that one of its values falls in, and a range with no documents should still be listed with count zero. For Total we want the count of documents that have a usable number or date, where NaN does not count as usable. Missing is the number of search hits with no usable value, including when the field is missing. Other is for documents that have a usable value but dont fall into any of the requested ranges.

For those number and date term facets we want each value once as text, numbers like 2.5 or -3 and dates as RFC 3339 in UTC like 2001-06-01T00:00:00Z, counted the same way as text terms.

We also get wrong results when searching over an index alias. Searching an alias of several indexes should give the exact same range and term facets as searching one index that has all those documents.
