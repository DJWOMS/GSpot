import { Requirement } from './Requirement'
import s from './Requirements.module.scss'

const Requirements = () => {
  return (
    <>
      <div className={s.requirements}>
        <div className={s.requirementsTabs}>
          <button className={s.requirementsTabsActive}>Windows</button>
          <button className={s.requirementsTabsButton}>Linux</button>
          <button className={s.requirementsTabsButton}>Apple</button>
        </div>

        <div>
          <Requirement
            title="Minimal requirements"
            list={{
              OS: 'Windows 7,Windows 8.1,Windows 10',
              Processor: 'Intel Core i5-2400s @ 2.5 GHz or AMD FX-6350 @ 3.9 GHz',
              Memory: 'Intel Core i5-2400s @ 2.5 GHz or AMD FX-6350 @ 3.9 GHz',
              Graphics: 'NVIDIA GeForce GTX 660 or AMD R9 270 (2048 MB VRAM with Shader Model 5.0)',
              'Disk Space': '42 GB available space',
              Architecture: 'Requires a 64-bit processor and OS',
              API: 'DirectX 11',
              Miscellaneous: 'Video Preset: Lowest (720p)',
            }}
          />

          <Requirement
            title="Recommended requirements"
            list={{
              OS: 'Windows 7,Windows 8.1,Windows 10',
              Processor: 'Intel Core i5-2400s @ 2.5 GHz or AMD FX-6350 @ 3.9 GHz',
              Memory: 'Intel Core i5-2400s @ 2.5 GHz or AMD FX-6350 @ 3.9 GHz',
              Graphics: 'NVIDIA GeForce GTX 660 or AMD R9 270 (2048 MB VRAM with Shader Model 5.0)',
              'Disk Space': '42 GB available space',
              Architecture: 'Requires a 64-bit processor and OS',
              API: 'DirectX 11',
              Miscellaneous: 'Video Preset: Lowest (720p)',
            }}
          />

          <div className="hidden">
            <Requirement
              title="Minimal requirements"
              list={{
                OS: 'Windows 7,Windows 8.1,Windows 10',
                Processor: 'Intel Core i5-2400s @ 2.5 GHz or AMD FX-6350 @ 3.9 GHz',
                Memory: 'Intel Core i5-2400s @ 2.5 GHz or AMD FX-6350 @ 3.9 GHz',
                Graphics: 'NVIDIA GeForce GTX 660 or AMD R9 270 (2048 MB VRAM with Shader Model 5.0)',
                'Disk Space': '42 GB available space',
                Architecture: 'Requires a 64-bit processor and OS',
                API: 'DirectX 11',
                Miscellaneous: 'Video Preset: Lowest (720p)',
              }}
            />

            <Requirement
              title="Recommended requirements"
              list={{
                OS: 'Windows 7,Windows 8.1,Windows 10',
                Processor: 'Intel Core i5-2400s @ 2.5 GHz or AMD FX-6350 @ 3.9 GHz',
                Memory: 'Intel Core i5-2400s @ 2.5 GHz or AMD FX-6350 @ 3.9 GHz',
                Graphics: 'NVIDIA GeForce GTX 660 or AMD R9 270 (2048 MB VRAM with Shader Model 5.0)',
                'Disk Space': '42 GB available space',
                Architecture: 'Requires a 64-bit processor and OS',
                API: 'DirectX 11',
                Miscellaneous: 'Video Preset: Lowest (720p)',
              }}
            />
          </div>

          <div className="hidden">
            <Requirement
              title="Minimal requirements"
              list={{
                OS: 'Windows 7,Windows 8.1,Windows 10',
                Processor: 'Intel Core i5-2400s @ 2.5 GHz or AMD FX-6350 @ 3.9 GHz',
                Memory: 'Intel Core i5-2400s @ 2.5 GHz or AMD FX-6350 @ 3.9 GHz',
                Graphics: 'NVIDIA GeForce GTX 660 or AMD R9 270 (2048 MB VRAM with Shader Model 5.0)',
                'Disk Space': '42 GB available space',
                Architecture: 'Requires a 64-bit processor and OS',
                API: 'DirectX 11',
                Miscellaneous: 'Video Preset: Lowest (720p)',
              }}
            />

            <Requirement
              title="Recommended requirements"
              list={{
                OS: 'Windows 7,Windows 8.1,Windows 10',
                Processor: 'Intel Core i5-2400s @ 2.5 GHz or AMD FX-6350 @ 3.9 GHz',
                Memory: 'Intel Core i5-2400s @ 2.5 GHz or AMD FX-6350 @ 3.9 GHz',
                Graphics: 'NVIDIA GeForce GTX 660 or AMD R9 270 (2048 MB VRAM with Shader Model 5.0)',
                'Disk Space': '42 GB available space',
                Architecture: 'Requires a 64-bit processor and OS',
                API: 'DirectX 11',
                Miscellaneous: 'Video Preset: Lowest (720p)',
              }}
            />
          </div>
        </div>
      </div>
    </>
  )
}

export { Requirements }
