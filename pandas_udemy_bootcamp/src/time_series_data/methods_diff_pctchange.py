''' The methods diff() and pct_change()
how to find absolute/relative changes in time series
using these methods '''
from shift_method import aapl


''' earlier we had used shift method with sub and div methods to find
abs and rel stock changes but pandas has 2 direct methods for the same
as shift is more general method '''
# absolute differences
print(aapl.AAPL.diff(periods=1))

aapl["Diff2"] = aapl.AAPL.diff(periods=1)
print(aapl.head(10))

# both are equal
print(aapl.Diff.equals(aapl.Diff2))

# relative differences
aapl["pct_change2"] = aapl.AAPL.pct_change(periods=1).mul(100)
print(aapl.head())

# monthly frequencies, first must resample our data
# first sample monthly data and then choose last record to compare with
# for more accuracy choose BM as B is businness days and stocks are
# traded on business days
# here we get monthy returns
aapl.AAPL.resample("BM").last().pct_change(periods=1).mul(100)
