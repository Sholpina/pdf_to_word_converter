# Import module

import groupdocs_conversion_cloud

# Get your app_sid and app_key at https://dashboard.groupdocs.cloud (free registration is required).

app_sid = "fe71c6cf-8ba6-48d6-ad9d-4c26638c8bcc"

app_key = "41c9425ce2348ba315fced351a55d97d"

# Create instance of the API

convert_api = groupdocs_conversion_cloud.ConvertApi.from_keys(app_sid, app_key)

file_api = groupdocs_conversion_cloud.FileApi.from_keys(app_sid, app_key)

try:

        #upload source file to storage

        filename = 'appealform.pdf'

        remote_name = 'appealform.pdf'

        output_name= 'appealform-out.docx'

        strformat='docx'

        request_upload = groupdocs_conversion_cloud.UploadFileRequest(remote_name,filename)

        response_upload = file_api.upload_file(request_upload)

        #Extract Text from PDF document

        settings = groupdocs_conversion_cloud.ConvertSettings()

        settings.file_path =remote_name

        settings.format = strformat

        settings.output_path = output_name

        request = groupdocs_conversion_cloud.ConvertDocumentRequest(settings)

        response = convert_api.convert_document(request)

        print("Document converted successfully: " + str(response))

except groupdocs_conversion_cloud.ApiException as e:

        print("Exception when calling get_supported_conversion_types: {0}".format(e.message))
