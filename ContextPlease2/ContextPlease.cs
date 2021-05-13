namespace ContextPlease2
{
    /// <summary>
    /// Primary class for ContextPlease, hosting the high level functionality of the program 
    /// </summary>
    public class ContextPlease
    {
        /// <summary>
        /// Produces the name of the program
        /// </summary>
        public static string Name => "Context Please";
        
        /// <summary>
        /// Returns the current version of the program
        /// </summary>
        public static string Version => "v2.0.0";
        
        /// <summary>
        /// Produces a link to the repository for the program
        /// </summary>
        public static string Link => "https://github.com/mbartelsman-dev/contextPlease";
        private Configuration Config { get; }
        
        /// <summary>
        /// Construct with a provided configuration object
        /// </summary>
        /// <param name="config">The configuration object for the program</param>
        public ContextPlease(Configuration config)
        {
            Config = config;
        }

        /// <summary>
        /// Handles the high level flow of the program
        /// </summary>
        public void Run()
        {
            JsonModel.JsonModel jsonModel = JsonModel.JsonModel
                .FromFile(Config.InputPath);
            
            RegistryModel.RegistryModel registryModel = RegistryModel.RegistryModel
                .FromJsonModel(jsonModel);

            registryModel
                .SerializeInstaller(Config.InstallerPath, Config.KeepOld);

            if (Config.MakeUninstaller)
            {
                registryModel
                    .SerializeUninstaller(Config.UninstallerPath);
            }
        }
    }
}
