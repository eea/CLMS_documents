"""Verify checks. Importing this package registers every check via @register.

To add a check, create a module here with a class decorated `@register` from
`pdf_to_qmd.verify`, then import it below.
"""

from . import frontmatter        # noqa: F401
from . import structural_counts  # noqa: F401
from . import figure_placement   # noqa: F401
from . import text_coverage      # noqa: F401
from . import table_coverage     # noqa: F401
from . import oversized_tables   # noqa: F401
from . import wide_table_legibility  # noqa: F401
