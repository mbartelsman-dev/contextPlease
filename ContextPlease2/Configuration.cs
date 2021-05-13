using System.IO;

namespace ContextPlease2
{
    /// <summary>
    /// Data class containing the configuration for ContextPlease
    /// </summary>
    public class Configuration
    {
        /// <summary>
        /// Path to the input JSON configuration file
        /// </summary>
        public string InputPath { get; }
        
        /// <summary>
        /// Path to the base output file name. Has no extension
        /// </summary>
        public string BaseOutputPath { get; }

        /// <summary>
        /// Should pre-existing registry keys be kept when writing new ones?
        /// </summary>
        public bool KeepOld { get; }
        
        /// <summary>
        /// Should an extra registry script for the removal of the described menu be created?
        /// </summary>
        public bool MakeUninstaller { get; }
        
        /// <summary>
        /// Path to the output installer file.
        /// </summary>
        public string InstallerPath => Path.Join(BaseOutputPath, ".install.reg");
        
        /// <summary>
        /// Path to the output uninstaller file.
        /// </summary>
        public string UninstallerPath => Path.Join(BaseOutputPath, ".remove.reg");

        /// <summary>
        /// Builds a new Settings object
        /// </summary>
        /// <param name="inputPath">Path to input file</param>
        /// <param name="baseOutputPath">Path to output file</param>
        /// <param name="keepOld">Should pre-existing registry keys be kept when writing new ones?</param>
        /// <param name="makeUninstaller">Should a removal registry script be generated?</param>
        public Configuration(
            string inputPath,
            string baseOutputPath,
            bool keepOld,
            bool makeUninstaller)
        {
            InputPath = inputPath;
            BaseOutputPath = baseOutputPath;
            KeepOld = keepOld;
            MakeUninstaller = makeUninstaller;
        }
    }
}
