# i have created this file stream_cipher
from django.http import HttpResponse
from django.shortcuts import render
# without template


def amit(requst):
    return HttpResponse("this is amit wala page")


# with template


def about(requst):
    return render(requst,  'about.html'
                  )


def index(requst):

    return render(requst, 'index.html')


def input_area(requst):
    return render(requst, 'i nput_text.html')


def output_area(requst):
    # retriving the input text that was entered by user in input_text.html that we had sent to analysed_text url with form ation with get method
    text = requst.GET.get('input_text', 'default')
    # storin  this string to dictionaly and sending it to the final result page output_text.html
    result = {'analysed_text': text}
    return render(requst, 'output_text.html', result)
