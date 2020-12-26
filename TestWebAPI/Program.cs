using System;
using System.IO;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Runtime.InteropServices;
using System.Threading.Tasks;
using System.Collections.Generic;
using System.Text;

using Dropbox.Api;
using Dropbox.Api.Common;
using Dropbox.Api.Files;
using Dropbox.Api.Team;
using NUnit.Framework;


namespace WebAPI
{
      public class TestWebAPI {

        [Test]
        public void testUpload(string filename = "MyTestFile.txt")
        {
            MyDropBoxApplication testObject = new MyDropBoxApplication();
            testObject.upload(filename);
        }

        [Test]
        public void testGetFileMetadata(string fileId)
        {
            MyDropBoxApplication testObject = new MyDropBoxApplication();
            testObject.getFileMetadata(fileId);
        }

        [Test]
        public void testDelete(string path)
        {
            MyDropBoxApplication testObject = new MyDropBoxApplication();
            testObject.delete(path);
        }

    }
    class Program {

        static void Main(string[] args)
        {
            TestWebAPI testWebAPI = new TestWebAPI(); 
            testWebAPI.testUpload("UploadTestFile.txt");
            testWebAPI.testGetFileMetadata("GetFileMetadataTestFile.txt");
            testWebAPI.testDelete("DeleteTestFile.txt");
        }
    }
}
