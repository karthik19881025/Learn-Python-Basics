words_up_to_19 = ['', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX',
                  'SEVEN', 'EIGHT', 'NINE', 'TEN', 'ELEVEN', 'TWELVE', 'THIRTEEN', 'FOURTEEN',
                  'FIFTEEN', 'SIXTEEN', 'SEVENTEEN', 'EIGHTEEN', 'NINETEEN']

words_for_tens = ['', '', 'TWENTY', 'THIRTY', 'FORTY', 'FIFTY', 'SIXTY', 'SEVENTY', 'EIGHTY', 'NINETY']

n = int(input('Enter a digit between 0 and 99: '))
output = ''
if n == 0:
    output = 'ZERO'
elif n <= 19:
    output = words_up_to_19[n+1]
elif n <= 99:
    output = words_for_tens[n // 10] + ' ' + words_up_to_19[n % 10]
else:
    output = 'Pls enter a value between 0 and 999'
print(output)
