select count(*)
from (
    select docid, count(term) c
    from (
        select distinct docid, term
        from frequency 
        where term in ('transactions', 'world')) a
    group by docid
    having c > 1) a;
