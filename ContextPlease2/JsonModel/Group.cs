namespace ContextPlease2.JsonModel
{
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
}
