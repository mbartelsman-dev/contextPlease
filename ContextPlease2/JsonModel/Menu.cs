namespace ContextPlease2.JsonModel
{
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
        public Menu[]? Menus { get; set; }
            
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
