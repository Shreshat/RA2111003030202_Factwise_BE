def number_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
             "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand"]

    def convert_below_1000(num):
        if num >= 100:
            return ones[num // 100] + "hundred" + (convert_below_1000(num % 100) if num % 100 > 0 else "")
        elif num >= 20:
            return tens[num // 10] + ones[num % 10]
        elif num >= 10:
            return teens[num - 10]
        else:
            return ones[num]

    if n == 1000:
        return "onethousand"
    elif n < 1000:
        return convert_below_1000(n)
    else:
        return "number out of range"

def count_letters_in_numbers_up_to(n):
    total_letters = 0
    for i in range(1, n + 1):
        words = number_to_words(i)
     
        letters_count = len(words.replace(" ", "").replace("-", ""))
        total_letters += letters_count
    return total_letters

total_letters_used = count_letters_in_numbers_up_to(1000)
print("Total letters that are used from 1 to 1000:", total_letters_used)
 





