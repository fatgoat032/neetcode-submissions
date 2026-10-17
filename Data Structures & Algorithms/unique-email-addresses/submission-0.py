class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_list = []
        for i in range(len(emails)):
            email, domain = emails[i].split("@")
            email = email.replace(".", "")
            email = email.split("+")[0]
            email_list.append(email + domain)
        print(email_list)
        email_set = set(email_list)
        return len(email_set)
