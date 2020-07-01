import mysql.connector

mydb = mysql.connector.connect(
  host="allyo-staging-rds-encrypted-aurora-cluster.cluster-ro-cpwl9sisckkw.us-west-2.rds.amazonaws.com",
  user="jaskeerat",
  passwd="jaskeerat@123",
  database="allyo_dev"
  )

# mycursor = mydb.cursor()
# sql = "select * from "
# print("hello")	
print(mydb)


    @patch('zeep.Client')
    def my_test(self, abc):
        request = self.factory.get('/api/v1/applicant/',
                                   HTTP_AUTHORIZATION=self.basic_authorization,
                                   HTTP_RETRIEVAL_ID="TEE-05",
                                   data={"external_applicant_id": 21770})

        abc.return_value = 'client_object'
        action = {'get': 'get'}
        from collections import OrderedDict
        auth_data = {
            'ats_auth': OrderedDict([('ats_name', 'taleo'), ('connector_type', 'ats'), ('client_id', 'scadmin'), ('client_secret', 'sc125tY%5u'), ('client_host', 'https://ptrdemo125.taleo.net'), ('retrieval_id', 'PITNEY_BOWES_POST'), ('ats_auth_type', 'BASIC')]), 'taleo': OrderedDict([('get_applicant', 'https://ptrdemo125.taleo.net/enterprise/soap?ServiceName=FindService&wsdl'), ('get_application', 'https://ptrdemo125.taleo.net/enterprise/soap?ServiceName=FindService&wsdl')]), 'meta_data': OrderedDict([('bulk_applicant', '{"metadata_list":[{"FILTER_CONFIG":{"TALEO_MEETS_BASICS_REQS":{"stages":["EXPLORED"]},"TALEO_HM_EMAIL_FILTER":{"hiring_manager_email":"nmglobal-scadmin@oracleads.com"},"TALEO_CANDIDATE_EMAIL_FILTER":{"candidate_email":"shubhamtest1@ttn.com"},"TALEO_REQUISITION_ID_FILTER":{"postings":["HWWTest001","SKTEST001"]},"TALEO_LOCATION_LIST_FILTER":{"location_codes":["VV"]},"TALEO_JOB_CATEGORIES_1":{"job_category_codes":["701"]},"TALEO_JOB_CATEGORIES_2":{"job_category_names":["Accounting"]}}}]}'), ('bulk_requisition', '{"metadata_list": [{"FILTER_CONFIG": {"TASK_PITNEY_BOWES_POST_PULL_APPLIED": {"postings": [], "status": [], "job_locations": [], "recruiter_emails": []}}}]}')]), 'key_mappings': OrderedDict([('bulk_requisition', OrderedDict([('allyo_to_ats_key', {'CLOSED': ['Canceled', 'Deleted'], 'DRAFT': ['Draft'], 'FILLED': ['Filled'], 'HOLD': ['On Hold'], 'OPEN': ['Open'], 'PENDING': ['Pending']}), ('ats_to_allyo_key', {'Canceled': ['CLOSED'], 'Deleted': ['CLOSED'], 'Draft': ['DRAFT'], 'Filled': ['FILLED'], 'On Hold': ['HOLD'], 'Open': ['OPEN'], 'Pending': ['PENDING']})]))]), 'external_applicant_id': '27367', 'retrieval_id': 'PITNEY_BOWES_POST', 'api_url_path': '/api/v1/applicant/?external_applicant_id=27367', 'api_endpoint_name': 'get_applicant', 'request_method': 'GET'}
        TaleoAuthenticationMethod().get_soap_service_object(
            auth_data=auth_data, api_endpoint_name='get_applicant',
            set_raw_response=True)
        self.assertEqual()
        # applicant_response = ApplicantApi.as_view(action)(request)

    # @patch('TaleoAuthenticationMethod.get_soap_service_object.Client')
    # def test_auth(self):
    #     from collections import OrderedDict
    #     auth_data = {'ats_auth': OrderedDict([('ats_name', 'taleo'), ('connector_type', 'ats'), ('client_id', 'scadmin'), ('client_secret', 'sc125tY%5u'), ('client_host', 'https://ptrdemo125.taleo.net'), ('retrieval_id', 'PITNEY_BOWES_POST'), ('ats_auth_type', 'BASIC')]), 'taleo': OrderedDict([('get_applicant', 'https://ptrdemo125.taleo.net/enterprise/soap?ServiceName=FindService&wsdl'), ('get_application', 'https://ptrdemo125.taleo.net/enterprise/soap?ServiceName=FindService&wsdl')]), 'meta_data': OrderedDict([('bulk_applicant', '{"metadata_list":[{"FILTER_CONFIG":{"TALEO_MEETS_BASICS_REQS":{"stages":["EXPLORED"]},"TALEO_HM_EMAIL_FILTER":{"hiring_manager_email":"nmglobal-scadmin@oracleads.com"},"TALEO_CANDIDATE_EMAIL_FILTER":{"candidate_email":"shubhamtest1@ttn.com"},"TALEO_REQUISITION_ID_FILTER":{"postings":["HWWTest001","SKTEST001"]},"TALEO_LOCATION_LIST_FILTER":{"location_codes":["VV"]},"TALEO_JOB_CATEGORIES_1":{"job_category_codes":["701"]},"TALEO_JOB_CATEGORIES_2":{"job_category_names":["Accounting"]}}}]}'), ('bulk_requisition', '{"metadata_list": [{"FILTER_CONFIG": {"TASK_PITNEY_BOWES_POST_PULL_APPLIED": {"postings": [], "status": [], "job_locations": [], "recruiter_emails": []}}}]}')]), 'key_mappings': OrderedDict([('bulk_requisition', OrderedDict([('allyo_to_ats_key', {'CLOSED': ['Canceled', 'Deleted'], 'DRAFT': ['Draft'], 'FILLED': ['Filled'], 'HOLD': ['On Hold'], 'OPEN': ['Open'], 'PENDING': ['Pending']}), ('ats_to_allyo_key', {'Canceled': ['CLOSED'], 'Deleted': ['CLOSED'], 'Draft': ['DRAFT'], 'Filled': ['FILLED'], 'On Hold': ['HOLD'], 'Open': ['OPEN'], 'Pending': ['PENDING']})]))]), 'external_applicant_id': '27367', 'retrieval_id': 'PITNEY_BOWES_POST', 'api_url_path': '/api/v1/applicant/?external_applicant_id=27367', 'api_endpoint_name': 'get_applicant', 'request_method': 'GET'}
    #     TaleoAuthenticationMethod().get_soap_service_object(
    #         auth_data=auth_data, api_endpoint_name='get_applicant',
    #         set_raw_response=True)
