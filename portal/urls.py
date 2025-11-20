"""
URL configuration for portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from portal import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # Week 1 Day 1 - Dictionaries & Counting APIs
    path('api/w1d1/count-character-frequency/', views.api_w1d1_count_character_frequency, name='api_w1d1_q1'),
    path('api/w1d1/count-word-frequency/', views.api_w1d1_count_word_frequency, name='api_w1d1_q2'),
    path('api/w1d1/top-3-frequent-words/', views.api_w1d1_top_3_frequent_words, name='api_w1d1_q3'),
    path('api/w1d1/count-without-stopwords/', views.api_w1d1_count_without_stopwords, name='api_w1d1_bonus1'),
    path('api/w1d1/top-5-words-across-strings/', views.api_w1d1_top_5_words_across_strings, name='api_w1d1_bonus2'),
    
    # Week 1 Day 2 - Functions & Error Handling APIs
    path('api/w1d2/safe-division/', views.api_w1d2_safe_division, name='api_w1d2_q4'),
    path('api/w1d2/find-maximum/', views.api_w1d2_find_maximum, name='api_w1d2_q5'),
    path('api/w1d2/is-palindrome/', views.api_w1d2_is_palindrome, name='api_w1d2_q6'),
    path('api/w1d2/count-numbers-frequency/', views.api_w1d2_count_numbers_frequency, name='api_w1d2_bonus3'),
    path('api/w1d2/has-mixed-case-and-number/', views.api_w1d2_has_mixed_case_and_number, name='api_w1d2_bonus4'),
    
    # Week 1 Day 3 - Regex & Pattern Recognition APIs
    path('api/w1d3/extract-emails/', views.api_w1d3_extract_emails, name='api_w1d3_q7'),
    path('api/w1d3/validate-phone-numbers/', views.api_w1d3_validate_phone_numbers, name='api_w1d3_q8'),
    path('api/w1d3/extract-dates/', views.api_w1d3_extract_dates, name='api_w1d3_q9'),
    path('api/w1d3/extract-emails-and-phones/', views.api_w1d3_extract_emails_and_phones, name='api_w1d3_bonus5'),
    path('api/w1d3/categorize-urls/', views.api_w1d3_categorize_urls, name='api_w1d3_bonus6'),
    
    # Assignment APIs
    path('api/assignment/q1/sentence-word-lengths/', views.api_assignment_q1_sentence_word_lengths, name='api_assignment_q1'),
    path('api/assignment/q2/common-elements/', views.api_assignment_q2_common_elements_in_lists, name='api_assignment_q2'),
    path('api/assignment/q3/count-unique-chars/', views.api_assignment_q3_count_unique_characters, name='api_assignment_q3'),
    path('api/assignment/q4/factorial/', views.api_assignment_q4_safe_factorial, name='api_assignment_q4'),
    path('api/assignment/q5/reverse-words/', views.api_assignment_q5_reverse_words, name='api_assignment_q5'),
    path('api/assignment/q6/validate-password/', views.api_assignment_q6_validate_password, name='api_assignment_q6'),
    path('api/assignment/q7/extract-hashtags/', views.api_assignment_q7_extract_hashtags, name='api_assignment_q7'),
    path('api/assignment/q8/remove-duplicates/', views.api_assignment_q8_remove_duplicates, name='api_assignment_q8'),
    path('api/assignment/q9/sum-numbers/', views.api_assignment_q9_sum_numbers_in_text, name='api_assignment_q9'),
    path('api/assignment/q10/find-anagrams/', views.api_assignment_q10_find_anagrams, name='api_assignment_q10'),
]
