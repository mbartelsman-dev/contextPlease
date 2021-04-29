using System;
using System.IO;
using System.Text.Json;
using System.Text.Json.Serialization;
namespace ContextPlease2
{
    public class JsonModel
    {
        /// <summary>
        /// Represents the root JSON element. Contains all model data within it
        /// </summary>
        public Root Model { get; set; }
        
        private JsonModel(Root model)
        {
            Model = model;
        }

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

            return new JsonModel(model);
        }
        
        /// <summary>
        /// Represents the root JSON element
        /// </summary>
        public class Root
        {
            public Group[] Groups { get; set; }
        }

        /// <summary>
        /// A group of menus and items that have a set of common targets
        /// </summary>
        public class Group
        {
            /// <summary>
            /// The targets that this group targets
            /// </summary>
            public string[] Targets { get; set; }
            
            /// <summary>
            /// The list of menus that are displayed for the targets of this group
            /// </summary>
            public Menu[] Menus { get; set; }
            
            /// <summary>
            /// The list of items that are displayed for the targets of this group
            /// </summary>
            public Item[] Items { get; set; }
        }

        /// <summary>
        /// A context menu sub-entry
        /// </summary>
        public class Item
        {
            /// <summary>
            /// The name to be displayed in the context menu
            /// </summary>
            public string Name { get; set; }
            
            /// <summary>
            /// The command that the item executes
            /// </summary>
            public string Command { get; set; }
            
            /// <summary>
            /// The path to the icon to be displayed, if any
            /// </summary>
            public string? Icon { get; set; }
            
            /// <summary>
            /// The preferred position of the entry, if any
            /// Must be one of: TOP, BOTTOM
            /// </summary>
            public string? Position { get; set; }
            
            /// <summary>
            /// Whether the entry is followed by a separator or not
            /// </summary>
            public bool HasSeparator { get; set; } = false;
        }
        
        /// <summary>
        /// A context menu submenu
        /// </summary>
        public class Menu
        {
            /// <summary>
            /// The name to be displayed in the context menu
            /// </summary>
            public string Name { get; set; }
            
            /// <summary>
            /// The list of menus that are nested under this one
            /// </summary>
            public Menu[] Menus { get; set; }
            
            /// <summary>
            /// The list of items that are under this menu
            /// </summary>
            public Item[] Items { get; set; }
            
            /// <summary>
            /// The path to the icon to be displayed, if any
            /// </summary>
            public string? Icon { get; set; }
            
            /// <summary>
            /// The preferred position of the entry, if any
            /// Must be one of: TOP, BOTTOM
            /// </summary>
            public string? Position { get; set; }
            
            /// <summary>
            /// Whether the entry is followed by a separator or not
            /// </summary>
            public bool HasSeparator { get; set; } = false;
        }
    }

}
