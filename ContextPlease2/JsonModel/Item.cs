namespace ContextPlease2.JsonModel
{
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
}
