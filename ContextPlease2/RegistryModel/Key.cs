using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using ContextPlease2.Extensions;
using ContextPlease2.JsonModel;

namespace ContextPlease2.RegistryModel
{
    /// <summary>
    /// A class representing a registry key
    /// </summary>
    public class Key
    {
        private Key(string name)
        {
            Name = name;
        }
        private string Name { get; init; }
        private Dictionary<string, string>? Values { get; init; }
        private List<Key>? Subkeys { get; init; }
            
        private const string NameKey = "MUIVerb";
        private const string IconKey = "Icon";
        private const string PositionKey = "Position";
        private const string SeparatorKey = "CommandFlags";
        private const string SeparatorValue = "0x40";
        private const string CommandPath = "command\\";
        private const string CommandKey = "@";
        private const string SubmenuPath = "shell\\";
        private const string PathPrefix = "CP";

        /// <summary>
        /// Converts the key to a list of string lines containing the installer data.
        /// </summary>
        /// <param name="prefix">Path where the keys should be in</param>
        /// <returns>A List of strings, one for each line</returns>
        public IEnumerable<string> InstallerLines(string prefix)
        {
            string path = Path.Combine(prefix, Name);
                
            var lines = new List<string> { $"[{path}]" };
                
            if (Values != null)
            {
                IEnumerable<string> values = Values.Select(pair => (pair.Key == SeparatorKey)
                    ? $"\"{pair.Key}\"={pair.Value}"
                    : "\"{pair.Key}\"=\"{pair.Value}\"");
                lines.AddRange(values);
            }

            if (Subkeys != null)
            {
                IEnumerable<string> values = Subkeys.SelectMany(key => key.InstallerLines(path));
                lines.AddRange(values);
            }

            return lines;
        }

        /// <summary>
        /// Converts the key to a list of string lines containing the uninstaller data.
        /// </summary>
        /// <param name="prefix">Path where the keys should be in</param>
        /// <returns>A List of strings, one for each line</returns>
        public IEnumerable<string> UninstallerLines(string prefix)
        {
            string path = Path.Combine(prefix, Name);
                
            return new List<string> { $"[-{path}]" };
        }

        /// <summary>
        /// Creates a list of Key trees from the data in a JSON Group object
        /// </summary>
        /// <param name="jsonGroup">The source of the data</param>
        /// <returns>The list of Keys</returns>
        public static IEnumerable<Key> FromJsonGroup(Group jsonGroup)
        {
            return jsonGroup.Targets
                .Select(target => BuildRoot(target, jsonGroup.Menus, jsonGroup.Items));
        }

        private static Key BuildRoot(string path, Menu[] jsonMenus, Item[] jsonItems)
        {
            var subKeys = new List<Key>();

            IEnumerable<Key> menus = jsonMenus
                .Select(BuildMenu);
            IEnumerable<Key> items = jsonItems
                .Select(BuildItem);

            subKeys.AddRange(menus);
            subKeys.AddRange(items);
                
            return new Key(Path.Combine(path, SubmenuPath))
            {
                Subkeys = subKeys
            };
        }

        private static Key BuildMenu(Menu jsonMenu)
        {
            string name = String.Concat(PathPrefix, jsonMenu.Name.ToSafeAscii());
                
            var values = new Dictionary<string, string>{ {NameKey, jsonMenu.Name} };
            if (jsonMenu.Icon != null) values[IconKey] = jsonMenu.Icon;
            if (jsonMenu.Position != null) values[PositionKey] = jsonMenu.Position;
            if (jsonMenu.HasSeparator) values[SeparatorKey] = SeparatorValue;

            var subKeys = new List<Key>{ BuildSubmenu(jsonMenu) };

            return new Key(name)
            {
                Values = values,
                Subkeys = subKeys
            };
        }

        private static Key BuildSubmenu(Menu jsonMenu)
        {
            var subKeys = new List<Key>();
                
            IEnumerable<Key> menus = jsonMenu.Menus
                .Select(BuildMenu);
            IEnumerable<Key> items = jsonMenu.Items
                .Select(BuildItem);

            subKeys.AddRange(menus);
            subKeys.AddRange(items);
                
            return new Key(SubmenuPath)
            {
                Subkeys = subKeys
            };
        }

        private static Key BuildItem(Item jsonItem)
        {
            string name = String.Concat(PathPrefix, jsonItem.Name.ToSafeAscii());
                
            var values = new Dictionary<string, string>{{NameKey, jsonItem.Name}};
            if (jsonItem.Icon != null) values[IconKey] = jsonItem.Icon;
            if (jsonItem.Position != null) values[PositionKey] = jsonItem.Position;
            if (jsonItem.HasSeparator) values[SeparatorKey] = SeparatorValue;

            var subKeys = new List<Key>{ BuildCommand(jsonItem.Command) };

            return new Key(name)
            {
                Values = values,
                Subkeys = subKeys
            };
        }

        private static Key BuildCommand(string command)
        {
            return new Key(CommandPath)
            {
                Values = new Dictionary<string, string> { { CommandKey, command } }
            };
        }
    }
}
