using System.IO;

namespace ContextPlease2
{
    public class ContextPlease
    {
        private Configuration Config { get; }
        
        public ContextPlease(Configuration config)
        {
            Config = config;
        }

        public void Run()
        {
            RegistryModel registryModel = JsonModel
                .FromFile(Config.InputPath)
                .ToRegistryModel();

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
