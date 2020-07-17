class Solution:
    def reformatDate(self, date: str) -> str:
        month = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}

        date = date.split(" ")

        for i in date[0]:
	        if(i.isalpha()):
		        date[0] = date[0].replace(i,'')
        if (len(date[0])==1):
            date[0] = '0'+ date[0]
        date[1] = month[date[1]]
        date.reverse()
        date = "-".join(date)
        
        return date
