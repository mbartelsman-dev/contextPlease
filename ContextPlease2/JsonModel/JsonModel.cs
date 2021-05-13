using System;
using System.IO;
using System.Text.Json;

namespace ContextPlease2.JsonModel
{
    /// <summary>
    /// This class represents the data of the JSON format used in ContextPlease
    /// </summary>
    public class JsonModel
    {
        /// <summary>
        /// Represents the root JSON element. Contains all model data within it
        /// </summary>
        public Root? Model { get; private init; }

        /// <summary>
        /// Generates a new JsonModel object from a file
        /// </summary>
        /// <param name="path">Path to the JSON file</param>
        /// <returns>The JsonModel object</returns>
        /// <exception cref="FormatException">If the JSON file does not follow the expected structure</exception>
        public static JsonModel FromFile(string path)
        {
            string fileData = File.ReadAllText(path);
            Root model = JsonSerializer.Deserialize<Root>(fileData)
                ?? throw new FormatException("The JSON file does not match the expected schema");

            return new JsonModel
            {
                Model = model
            };
        }
    }
}
