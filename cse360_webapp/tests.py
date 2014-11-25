from django.test import TestCase, Client 
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse
from datetime import datetime
from django.http import HttpResponse 

class cse360_webapp_test(TestCase): 
    def test_login_view(self): 
        client = Client()
        url = reverse('cse360_webapp.views.login') 
        home_url = reverse('app1.views.events')
        resp = self.client.get(url) 
        resp_home = self.client.get(home_url)
        
        #Make sure that we arrive at the login page 
        self.assertEqual(resp.status_code, 200)  
        #Make sure that request for home is redirected
        self.assertEqual(resp_home.status_code, 302) 
        
        user = User.objects.create_user(username="test_user", password="password")
        #self.client.login(username='test_user', password='password')
        resp_login = self.client.post('/accounts/login/', {'username':'test_user', 'password':'password'})
        #Try again to get to login and home page 
        resp = self.client.get(url) 
        resp_home = self.client.get(home_url)
        
        #Check that we're able to login successfully 
        self.assertEqual(resp_login.status_code, 200)
        self.client.login(username='test_user', password='password')
        s = self.client.session; s['lin'] = 'lin'; s.save()
        resp_login = self.client.get('/accounts/login/')
        #Now that we're logged in, view will redirect 
        self.assertEqual(resp_login.status_code, 302)
        
    def test_logout_view(self): 
        client = Client() 
        user = User.objects.create_user(username="test_user", password="password")
        resp_login = self.client.post('/accounts/login/', {'username':'test_user', 'password':'password'})
        self.client.login(username='test_user', password='password')
        resp_logout = self.client.get('/accounts/logout/')
    
        self.assertEqual(resp_logout.status_code, 200)
        
    def test_invalid_view(self): 
        client = Client() 
        user = User.objects.create_user(username="test_user", password="password")
        self.client.login(username="test_user", password="password")
        resp = self.client.get('/accounts/invalid/') 
        
        self.assertEqual(resp.status_code, 200) 
        
    def test_register_view(self): 
        client = Client() 
        #self.client = Client(enforce_csrf_checks=True)
        resp = self.client.get('/accounts/register/')
        #csrf_token = self.client.cookies['csrftoken'].value
        resp = self.client.post('/accounts/register/', 
        {'username':'test_user@email', 'password':'password1', 'password2':'password'}) 
                
        self.assertEqual(resp.status_code, 200)    
        #self.assertEqual(resp['Location'], 'http://localhost:8000/accounts/register_success/')
        #self.assertEqual('/accounts/register_success/', resp.__getitem__('Location'))
        #self.assertRedirects(resp, reverse('/accounts/register_success/'), status_code=200, target_status_code=200, msg_prefix='')
        #TestCase.assertRedirects(response, expected_url, status_code=302, target_status_code=200, msg_prefix='')
        
    def test_register_success(self): 
        client = Client() 
        resp = self.client.get('/accounts/register_success/') 
        
        self.assertEqual(resp.status_code, 200) 
        
    def test_auth_view(self): 
        client = Client() 
        user = User.objects.create_user(username='test_user', password='password') 
        self.client.login(username='test_user', password='password')
        url = reverse('cse360_webapp.views.auth_view') 
        resp = self.client.post(url, {'username':'test_user', 'password':'password'}) 
        
        self.assertEqual(resp.status_code, 302) 
        self.assertRedirects(resp,'/home/', status_code=302, target_status_code=200, msg_prefix='')
        
        
        
