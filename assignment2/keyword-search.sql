select sum(count) score
from frequency
where term in ('washington', 'taxes', 'treasury')
group by docid
order by score desc
limit 1;
