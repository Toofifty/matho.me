import string
import random

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from django.contrib.auth.decorators import login_required

from .forms import URLForm
from .models import UrlRecord
from personal_webpage.urls import pages

# Generate a new short URL of specified size
# Possible characters are in chars, which by
# default contains a-z A-Z 0-9
# Also ensures new URL isn't already in the
# database
def gen_url(size, chars=string.ascii_uppercase+string.ascii_lowercase):
    while True:
        # Generate string
        url = ''.join(random.choice(chars) for _ in range(size))
        # Find all matches in database
        existing = UrlRecord.objects.filter(short_url=url)
        # Continue loop if URL exists
        if not existing: 
            break
    return url
        
# A user needs to be authenticated to view
# the list and add/delete URLs, using this
# decorator we can auto redirect an anonymous
# user to the login page and back
@login_required
# Page to display all URLs owned by the user
# and forms/buttons to create and delete URLs
def index(request, short_url=None):
    # Error message to be displayed
    error = None
        
    # New URL form ends up here
    if request.method == 'POST':
        form = URLForm(request.POST)
        
        if form.is_valid():
            new_short_url = form.cleaned_data['short_url']
            
            # Get list of objects that match the URL
            # will be empty if new URL is not a duplicate
            existing = UrlRecord.objects.filter(
                short_url=new_short_url)
                
            # Check if URL starts with one of the
            # default pages
            valid = True
            for page in pages:
                if new_short_url.startswith(page):
                    valid = False
                    error = 'URL cannot start with "' + page +'".'
                
            if valid:
                if not existing:
                    new_long_url = form.cleaned_data['long_url']
                    
                    # Ensure long URL contains a proper header
                    if not '://' in new_long_url:
                        new_long_url = 'http://' + new_long_url
                    
                    # Create and save record
                    url = UrlRecord(short_url=new_short_url,
                            long_url=new_long_url, user=request.user)
                    url.save()
                    
                else:
                    error = 'URL "' + new_short_url + '" already exists.'
                
        else:
            # Catches any error not caught in the
            # HTML form
            error = 'Invalid URL'
            
    # short_url is not None when a request 
    # to remove an item is given
    # This is done here to prevent duplicate
    # code in the remove method (need to end
    # up on the same HTML page anyway)
    if short_url is not None:
        try:
            # Get the UrlRecord that matches the url
            url_record = UrlRecord.objects.get(short_url=short_url)
            # Ensure record exists and user
            # owns this URL to delete it
            if url_record is not None and url_record.user == request.user:
                url_record.delete()
        except:
            # Very generic
            error = 'Failed to delete ' + short_url
            short_url = None
            
    # Retrieve a list of URLs that the user owns
    user_urls = UrlRecord.objects.filter(user=request.user)
    
    # current_site = Site.objects.get_current()
    return render(request, 'urls/index.html', {
        'user_urls': user_urls, 'site_domain': request.get_host()[:-3], 
        'generated_url': gen_url(4), 'deleted_url': short_url, 'error': error})

@login_required
# Create a new, random URL from the address given
def new(request, long_url):
    url = UrlRecord(short_url=gen_url(4), long_url=long_url, user=request.user)
    url.save()
    return render(request, 'urls/new.html', {"short_url": url.short_url})
    
# Returns the index page with parameter 
# to remove the specified URL
def remove(request, short_url):
    return index(request, short_url)
    
# Redirects to the long URL found in
# the database, and increments the
# redirect counter
def redir(request, short_url):
    u = get_object_or_404(UrlRecord, short_url=short_url)
    u.redirects += 1
    u.save()
    return HttpResponseRedirect(u.long_url)