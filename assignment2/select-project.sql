select count(*)
from (
    select *
    from frequency
    where docid = '10398_txt_earn' and count=1) a;
