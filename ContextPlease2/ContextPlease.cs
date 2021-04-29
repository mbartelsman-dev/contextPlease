using System.IO;

namespace ContextPlease2
{
    /// <summary>
    /// Primary class for ContextPlease, hosting the high level functionality of the program 
    /// </summary>
    public class ContextPlease
    {
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
            JsonModel jsonModel = JsonModel
                .FromFile(Config.InputPath);
            
            RegistryModel registryModel = RegistryModel
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
