select count(*)
from (
    select sum(count) c
    from frequency
    group by docid
    having c > 300) a;
