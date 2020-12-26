using System;
using System.Collections.Generic;
using System.Text;
//AnusualSilverSnowTestWithThreeEndpoints aka MyDropBoxApplication

namespace WebAPI
{

    public class MyDropBoxApplication
    {

        // URL STRUCTURE: https://content.dropboxapi.com/2/files/upload
        public void upload(string filename)
        {
            //  Присоединение к dropboxapi
            Chilkat.Rest chilkatRest = new Chilkat.Rest();
            bool isSuccess = chilkatRest.Connect("content.dropboxapi.com", 403, true, true);
            if (!isSuccess)
            {
                Console.WriteLine("Connection failure: " + Convert.ToString(chilkatRest.LastErrorText));
                return /*"Connection to dropboxapi failed"*/;
            }

            //  Добавление заголовков и параметров:
            Chilkat.JsonObject jsonObject = new Chilkat.JsonObject();
            chilkatRest.AddHeader("Authorization", "Bearer jvhy3dm9ExsAAAAAAAAAAZ0Jm0J5N-H_8YlCPFPJklMZsSUqY7xCnOrpfI9-RR2d");
            chilkatRest.AddHeader("Dropbox-API-Arg", jsonObject.Emit());
            chilkatRest.AddHeader("Content-Type", "application/octet-stream");
            jsonObject.AppendString("path", "/" + filename);
            jsonObject.AppendString("mode", "add");
            jsonObject.AppendBool("autorename", true);
            jsonObject.AppendBool("mute", false);
            //  Можно ещё добавить property_groups и strict_conflict, но нет смысла усложнять.         

            //  Попытаемся загрузить файл на сервер. Попытка непосредственной реализации Upload.
            Chilkat.Stream chilkatStream = new Chilkat.Stream();
            chilkatStream.SourceFile = filename;
            string responseString = chilkatRest.FullRequestStream("POST", "/2/files/upload", chilkatStream);
            if (!chilkatRest.LastMethodSuccess) {
                Console.WriteLine(chilkatRest.LastErrorText);
                return/* "Unsuccess uploading"*/;
            }

            //  Если что-то пошло не так, то код ответа будет отличный от 200.
            //  Тогда нам следует получить более подробную информацию о том, что именно пошло не так.
            if (chilkatRest.ResponseStatusCode != 200) {
                Console.WriteLine("Response code: " + Convert.ToString(chilkatRest.ResponseStatusCode));
                Console.WriteLine("Response text: " + chilkatRest.ResponseStatusText);
                Console.WriteLine("Response header: " + chilkatRest.ResponseHeader);
                return/* "Response code is not 200"*/;
            }

        }


        // URL STRUCTURE: https://api.dropboxapi.com/2/sharing/get_file_metadata
        // fileId == String(min_length=1, pattern="((/|id:).*|nspath:[0-9]+:.*)|ns:[0-9]+(/.*)?")
        public void getFileMetadata(string fileId)
        {
            //  Присоединение к dropboxapi
            Chilkat.Rest chilkatRest = new Chilkat.Rest();
            bool isSuccess = chilkatRest.Connect("api.dropboxapi.com", 403, true, true);
            if (!isSuccess)
            {
                System.Diagnostics.Debug.WriteLine("Connection failure: " + Convert.ToString(chilkatRest.LastErrorText));
                System.Diagnostics.Debug.WriteLine("Reason of failure: " + Convert.ToString(chilkatRest.ConnectFailReason));
                return /*"Connection to dropboxapi failed"*/;
            }

            //  Добавление заголовков и параметров:
            Chilkat.JsonObject jsonObject = new Chilkat.JsonObject();
            chilkatRest.AddHeader("Authorization", "Bearer jvhy3dm9ExsAAAAAAAAAAZ0Jm0J5N-H_8YlCPFPJklMZsSUqY7xCnOrpfI9-RR2d");
            chilkatRest.AddHeader("Content-Type", "application/json");
            jsonObject.UpdateString("file", fileId);

            //  Пытаемся получить метаданные файла. Попытка реализации запроса GetFileMetadata
            Chilkat.StringBuilder requestBody = new Chilkat.StringBuilder();
            Chilkat.StringBuilder responseBody = new Chilkat.StringBuilder();
            jsonObject.EmitSb(requestBody);
            isSuccess = chilkatRest.FullRequestSb("POST", "/2/files/get_file_metadata", requestBody, responseBody);
            if (!isSuccess)
            {
                System.Diagnostics.Debug.WriteLine("Request failure: " + Convert.ToString(chilkatRest.LastErrorText));
                return /*"GetFileMetadata request failure"*/;
            }

            //  Если что-то пошло не так, то код ответа будет отличный от 200.
            //  Тогда нам следует получить более подробную информацию о том, что именно пошло не так.
            if (chilkatRest.ResponseStatusCode != 200)
            {
                Console.WriteLine("Response code: " + Convert.ToString(chilkatRest.ResponseStatusCode));
                Console.WriteLine("Response text: " + chilkatRest.ResponseStatusText);
                Console.WriteLine("Response header: " + chilkatRest.ResponseHeader);
                return /*"Response code is not 200"*/;
            }

        }


        // URL STRUCTURE: https://api.dropboxapi.com/2/files/delete_v2
        public void delete(string path)
        {
            //  Присоединение к dropboxapi
            Chilkat.Rest chilkatRest = new Chilkat.Rest();
            bool isSuccess = chilkatRest.Connect("api.dropboxapi.com", 403, true, true);
            if (!isSuccess) {
                Console.WriteLine("Connection failure: " + Convert.ToString(chilkatRest.LastErrorText));
                return /*"Connection to dropboxapi failed"*/;
            }

            //  Добавление заголовков и параметров:
            Chilkat.JsonObject jsonObject = new Chilkat.JsonObject();
            chilkatRest.AddHeader("Authorization", "Bearer jvhy3dm9ExsAAAAAAAAAAZ0Jm0J5N-H_8YlCPFPJklMZsSUqY7xCnOrpfI9-RR2d");
            chilkatRest.AddHeader("Content-Type", "application/json");
            jsonObject.UpdateString("path", path);

            //  Пытаемся удалить файл. Попытка реализации запроса Delete
            Chilkat.StringBuilder requestBody = new Chilkat.StringBuilder();
            Chilkat.StringBuilder responseBody = new Chilkat.StringBuilder();
            jsonObject.EmitSb(requestBody);
            isSuccess = chilkatRest.FullRequestSb("POST", "/2/files/delete_v2", requestBody, responseBody);
            if (!isSuccess) {
                System.Diagnostics.Debug.WriteLine("Request failure: " + Convert.ToString(chilkatRest.LastErrorText));
                return /*"Delete request failure"*/;
            }

            //  Если что-то пошло не так, то код ответа будет отличный от 200.
            //  Тогда нам следует получить более подробную информацию о том, что именно пошло не так.
            if (chilkatRest.ResponseStatusCode != 200) {
                Console.WriteLine("Response code: " + Convert.ToString(chilkatRest.ResponseStatusCode));
                Console.WriteLine("Response text: " + chilkatRest.ResponseStatusText);
                Console.WriteLine("Response header: " + chilkatRest.ResponseHeader);
                return/* "Response code is not 200"*/;
            }
        }

    }
}