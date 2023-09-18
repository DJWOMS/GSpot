import { ChangeEventHandler, useMemo } from 'react'
import { IconArrowDown, IconArrowUp } from '@tabler/icons-react'
import {
  ColumnDef,
  flexRender,
  getCoreRowModel,
  getPaginationRowModel,
  OnChangeFn,
  PaginationState,
  SortingState,
  useReactTable,
} from '@tanstack/react-table'
import cn from 'classnames'
import s from './Table.module.css'

export type SortingType<T> = {
  id: keyof T
  desc: boolean
}[]

type NavigationProps = {
  pageSizes?: number[]
  pageCount: number
  pagination: PaginationState
  setPagination: OnChangeFn<PaginationState>
}

interface Props<T> {
  data: T[]
  columns: ColumnDef<T>[]
  navigation?: NavigationProps
  sorting?: SortingType<T>
  setSorting?: OnChangeFn<SortingType<T>>
  className?: string
}

const Table = <T,>({ columns, data, setSorting, sorting, navigation, className }: Props<T>): JSX.Element => {
  const memoizedColumns = useMemo(
    () =>
      columns.map((i) => ({
        ...i,
        enableSorting: i.enableSorting ?? false,
        cell: i.cell ?? ((v) => v.getValue()),
      })),
    [columns]
  )

  const table = useReactTable({
    state: {
      sorting: sorting as SortingState | undefined,
      pagination: navigation?.pagination,
    },
    pageCount: navigation?.pageCount,
    data,
    columns: memoizedColumns,
    getCoreRowModel: getCoreRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    manualSorting: true,
    manualPagination: true,
    onPaginationChange: navigation?.setPagination,
    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
    // @ts-ignore
    onSortingChange: setSorting,
  })

  const onSelectPageSize: ChangeEventHandler<HTMLSelectElement> = (e) => {
    if (navigation?.setPagination) {
      navigation.setPagination((prev) => ({
        ...prev,
        pageSize: Number(e.target.value),
      }))
    }
  }

  return (
    <div className={s.wrapper}>
      <div className={s.outer}>
        <div className={s.inner}>
          <div className={s.container}>
            <table className={cn(s.table, className)}>
              <thead className={s.tableHead}>
                {table.getHeaderGroups().map((headerGroup) => (
                  <tr key={headerGroup.id}>
                    {headerGroup.headers.map((header) => (
                      <th key={header.id} className={s.tableHeadColumn}>
                        {header.isPlaceholder ? null : (
                          <div
                            {...{
                              className: header.column.getCanSort() ? s.tableHeadSort : '',
                              onClick: header.column.getToggleSortingHandler(),
                            }}
                          >
                            {flexRender(header.column.columnDef.header, header.getContext())}
                            {{
                              asc: <IconArrowDown />,
                              desc: <IconArrowUp />,
                            }[header.column.getIsSorted() as string] ?? null}
                          </div>
                        )}
                      </th>
                    ))}
                  </tr>
                ))}
              </thead>
              <tbody>
                {table.getRowModel().rows.map((row) => (
                  <tr key={row.id} className={s.tableBodyCell}>
                    {row.getVisibleCells().map((cell) => (
                      <td className={s.tableBodyColumn} key={cell.id}>
                        {flexRender(cell.column.columnDef.cell, cell.getContext())}
                      </td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
            {navigation ? (
              <>
                <div className={s.navigationSeparator} />
                <div className={s.navigationContainer}>
                  <button
                    className={s.navigationBtn}
                    onClick={() => table.previousPage()}
                    disabled={!table.getCanPreviousPage()}
                  >
                    {'<'}
                  </button>
                  <button
                    className={s.navigationBtn}
                    onClick={() => table.nextPage()}
                    disabled={!table.getCanNextPage()}
                  >
                    {'>'}
                  </button>
                  <span className={s.navigationPage}>
                    <div>Страница</div>
                    <strong>
                      {table.getState().pagination.pageIndex + 1} из {table.getPageCount()}
                    </strong>
                  </span>
                  {navigation.pageSizes && (
                    <select
                      className={s.navigationSelect}
                      value={table.getState().pagination.pageSize}
                      onChange={onSelectPageSize}
                    >
                      {navigation.pageSizes.map((pageSize) => (
                        <option key={pageSize} value={pageSize}>
                          Показывать {pageSize} элементов
                        </option>
                      ))}
                    </select>
                  )}
                  <div className="h-4" />
                </div>
              </>
            ) : null}
          </div>
        </div>
      </div>
    </div>
  )
}

export default Table
